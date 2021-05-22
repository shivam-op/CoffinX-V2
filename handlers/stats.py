import asyncio
import os
import subprocess
import time

import psutil
from pyrogram import filters

from handlers import bot_start_time

async def bot_sys_stats():
    bot_uptime = int(time.time() - bot_start_time)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    stats = f"""
 𝘾𝙊𝙁𝙁𝙄𝙉 𝙓 𝙈𝙐𝙎𝙄𝘾
------------------
𝙲𝙾𝙵𝙵𝙸𝙽 𝚄𝙿𝚃𝙸𝙼𝙴: {formatter.get_readable_time((bot_uptime))}
𝙱𝙾𝚃: {round(process.memory_info()[0] / 1024 ** 2)} MB
𝙲𝙿𝚄: {cpu}%
𝚁𝙰𝙼: {mem}%
𝙳𝙸𝚂𝙺: {disk}%
A Bᴏᴛ Bʏ Tᴇᴀᴍ Cᴏғғɪɴ 👨‍💻
"""   
    
@Client.on_message(filters.user(SUDO_USER)& filters.command("stats"))
async def get_stats(_, message):
    stats = await bot_sys_stats()
    await message.reply_text(stats)
