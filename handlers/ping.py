from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton 


@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def help(_, message: Message):
    await message.reply_text(
        f"""**Contact me in PM to get command**""")
        reply_markup=InlineKeyboardMarkup
            [
                [
                    InlineKeyboardButton(
                        "press here 🔰", url="t.me/Try_music_robot?start=help"
                    )
                ]
            ]
        ),
    )
