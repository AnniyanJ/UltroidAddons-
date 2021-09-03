# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

# Pixelator Plugin
# https://stackoverflow.com/questions/55508615/how-to-pixelate-image-using-opencv-in-python

"""
✘ Commands Available -

• `{i}pixelator <reply image>`
    Create a Pixelated Image..
"""

import cv2
from . import *
import os


@ultroid_cmd(pattern="pixelator ?(.*)")
async def pixelator(event):
    reply_message = await event.get_reply_message() 
    if not (reply_message and reply_message.photo):
        return await eor(event, "`Reply to a photo`")
    try:
        hw = int(event.pattern_match.group(1))
    except (ValueError, TypeError):
        hw = 50
    input_ = cv2.imread('images/paddington.png')
    height, width = input_.shape[:2]
    w, h = (hw, hw)
    temp = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR)
    output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    cv2.imwrite("output.jpg", output)
    await eor(event, "• Pixelated by Ultroid", file="output.jpg")
    os.remove("output.jpg")