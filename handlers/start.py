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
                        "help 🆘", callback_data="bot_commands")
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

@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = 'help', callback_data = "get_help")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/Coffinxsupport"
        button = [
            [InlineKeyboardButton("Take me to Your group 👨‍💻", url=f"https://t.me/CoffinXmusic_bot?startgroup=true")],
            [InlineKeyboardButton(text = '📲 Updates', url=f"https://t.me/CoffinX_updates"),
             InlineKeyboardButton(text = '💬 Support', url=f"https://t.me/Coffinxsupport")],
            [InlineKeyboardButton(text = '👨‍💻 Creator', url=f"https://t.me/Shashank_xxD")],
            [InlineKeyboardButton(text = '◀️', callback_data = f"get_help")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '▶️', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**🙋‍♀️ Hello there! I can play music in the voice chats of telegram groups & channels.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🟡 Click here for help 🟡", url=f"https://t.me/Coffinxmusic_bot?start"
                    )
                ]
            ]
        ),
    )

@app.on_callback_query(filters.regex("bot_commands"))
async def commands_callbacc(_, CallbackQuery):
    text, keyboard = await help_parser(CallbackQuery.from_user.mention)
    await app.send_message(
        CallbackQuery.message.chat.id, text=text, reply_markup=keyboard
    )

    await CallbackQuery.message.delete()    
