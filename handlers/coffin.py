from asyncio import sleep
from pyrogram import filters
from pyrogram.handlers import MessageHandler
from config import SUDO_USERS, BANNED
from strings import get_string as _


async def n4u(client, message):
    m = await message.reply_text(_("coffin"))

    if m and message.chat.type != "private":
        await sleep(5)
        await m.delete()

        try:
            await message.delete()
        except:
            pass


__handlers__ = [
    [
        MessageHandler(
            n4u,
            (filters.command("pause", "/")
             | filters.command("skip", "/")
             | filters.command("resume", "/")
             | filters.command("stream", "/")
             | filters.command("bans", "/")
             | filters.command("ban", "/")
             | filters.command("unban", "/")
             | filters.command("cleardownloads", "/")
             | filters.command("play", "/")
             | filters.command("r", "/"))
            & ~ SUDO_FILTER
            & ~ BANNED
        )
    ]
]
