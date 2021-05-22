@Client.on_message(filters.command("help") & filters.group & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
      """**Hey Contact Me In Pm For Help**""".
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " help 🆘", url="https://t.me/CoffinXmusic_bot?start=help"
                    )
                ]
            ]
        ),
    )      
