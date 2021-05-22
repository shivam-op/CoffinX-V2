import asyncio
import os
import subprocess
import time

import psutil
from pyrogram import filters

from handlers import (bot_start_time)

async def bot_sys_stats():
    bot_uptime = int(time.time() - bot_start_time)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    stats = f"""
 𝙃𝙄𝙉𝘼𝙏𝘼 𝘽𝙊𝙏
------------------
𝙷𝙸𝙽𝙰𝚃𝙰 𝚄𝙿𝚃𝙸𝙼𝙴: {formatter.get_readable_time((bot_uptime))}
𝙱𝙾𝚃: {round(process.memory_info()[0] / 1024 ** 2)} MB
𝙲𝙿𝚄: {cpu}%
𝚁𝙰𝙼: {mem}%
𝙳𝙸𝚂𝙺: {disk}%
𝙰 𝙱𝙾𝚃 𝙱𝚈 𝚃𝙴𝙰𝙼 𝙲𝙾𝙵𝙵𝙸𝙽 👨‍💻
"""   
    
@Client.on_message(filters.user(SUDO_USER)& filters.command("stats"))
async def get_stats(_, message):
    stats = await bot_sys_stats()
    await message.reply_text(stats)
