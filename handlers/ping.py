from datetime import datetime
from time import time

from pyrogram import Client, filters, emoji
from pyrogram.types import Message

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

self_or_contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)


# https://gist.github.com/borgstrom/936ca741e885a1438c374824efb038b3
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(filters.command("ping") & filters.group & ~filters.edited)
async def get_uptime(_, m: Message):
    """Reply ping with pong and delete both messages"""
    start = time()
    m_reply = await m.reply_text("...")
    delta_ping = time() - start
    await m_reply.edit_text(
        f"ＰＯＮＧ!!\n"
        f"{emoji.ROBOT} 𝙿𝙸𝙽𝙶: `{delta_ping * 1000:.3f} 𝚖𝚜`"
    )


@Client.on_message(filters.command("uptime") & filters.group & ~filters.edited)
async def ping_pong(_, m: Message):
    """/ping"""
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        f"ＵＰＴＩＭＥ\n"
        f"- 𝙲𝙾𝙵𝙵𝙸𝙽 𝚄𝙿𝚃𝙸𝙼𝙴: `{uptime}`\n"
        f"- 𝚂𝚃𝙰𝚁𝚃 𝚃𝙸𝙼𝙴: `{START_TIME_ISO}`"
    )
"""
__mod_name__ = "ping/uptime"

__help__ = 
𝙿𝙸𝙽𝙶 𝙰𝙽𝙳 𝚄𝙿𝚃𝙸𝙼𝙴 

__command_list__ = ["ping"], ["uptime"]
"""

