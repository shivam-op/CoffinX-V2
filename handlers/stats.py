from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("stats") & filters.group & ~filters.private & ~filters.channel)
async def gstats(_, message: Message):
    await message.reply_text(
      f"""𝙃𝙄𝙉𝘼𝙏𝘼 𝘽𝙊𝙏
------------------
𝙷𝙸𝙽𝙰𝚃𝙰 𝚄𝙿𝚃𝙸𝙼𝙴: {formatter.get_readable_time((bot_uptime))}
𝙱𝙾𝚃: {round(process.memory_info()[0] / 1024 ** 2)} MB
𝙲𝙿𝚄: {cpu}%
𝚁𝙰𝙼: {mem}%
𝙳𝙸𝚂𝙺: {disk}%
𝙰 𝙱𝙾𝚃 𝙱𝚈 𝚃𝙴𝙰𝙼 𝙲𝙾𝙵𝙵𝙸𝙽 👨‍💻
"""
