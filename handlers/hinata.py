from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""➼ Helloowww 👋 {message.from_user.first_name}! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\n➼ Do you want me to play music in your Telegram groups'voice chats? Please click the " cσммαη∂s " button below to know how you can use me.\n\n➼ Use the buttons below to know more about me ❤️🔥\n\n➼ For any Help [Coffin X Support](https://t.me/CoffinXsupport)\n\nA project by Team Coffin""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "Stats 👨‍💻", callback_data="stats_callback")
                  ],[
                    InlineKeyboardButton(
                        "🚑 Support Group 🚑", url="https://t.me/aboutoxy"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🔥 Take me to ur group 🔥", url="https://t.me/CoffinXmusic_bot?groupstart=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Yoo Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "SUPPORT GROUP", url="https://t.me/CoffinXsupport")
                ]
            ]
        )
   )

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
      await message.reply_text("""**Cᴏɴᴛᴀᴄᴛ ᴍᴇ ɪɴ ᴘᴍ ғᴏʀ ʜᴇʟᴘ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🆘 help 🆘", url="https://t.me/CoffinX_music?start=help")
                ]
            ]
        )
   )
