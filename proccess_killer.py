# Ultroid - UserBot
# Copyright (C) 2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available
• `{i}pkill <proccess name>`
    Kill the given proccess name.
"""


from . import *
import psutil , os, signal


@ultroid_cmd(pattern="pkill ?(.*)")
async def _(event):
    pname = event.pattern_match.group(1)
    if not pname:
        return await event.eor("`Give Any Proccess Name To Kill it`")
    await event.eor("`Killing The Proccess Named` **{pname}**")
    for p in psutil.process_iter():
        pnames = p.name()
        if pnames == pname:
            os.kill(p.pid, signal.SIGKILL)
            return await event.edit("`Successfully Killed The Proccess Named` **{pname}**")
    return await event.edit("`Given Proccess Not Found`")
