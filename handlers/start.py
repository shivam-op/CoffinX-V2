# OxyXmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



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
                        "help 🆘", callback_data="get_help")
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

@register(regexp="get_help", f="cb")
@get_strings_dec("pm_menu")
async def help_cb(event, strings):
    button = help_markup(MOD_HELP)
    button.add(InlineKeyboardButton(strings["back"], callback_data="go_to_start"))
    with suppress(MessageNotModified):
        await event.message.edit_text(strings["help_header"], reply_markup=button)


@register(regexp="lang_btn", f="cb")
async def set_lang_cb(event):
    await select_lang_keyboard(event.message, edit=True)


@register(regexp="go_to_start", f="cb")
async def back_btn(event):
    await get_start_func(event, edit=True)


@register(cmds="help", only_pm=True)
@disableable_dec("help")
@get_strings_dec("pm_menu")
async def help_cmd(message, strings):
    button = help_markup(MOD_HELP)
    button.add(InlineKeyboardButton(strings["back"], callback_data="go_to_start"))
    await message.reply(strings["help_header"], reply_markup=button)


@register(cmds="help", only_groups=True)
@disableable_dec("help")
@get_strings_dec("pm_menu")
async def help_cmd_g(message, strings):
    text = strings["btn_group_help"]
    button = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text=text, url="https://t.me/CoffinXmusic_bot?start")
    )
    await message.reply(strings["help_header"], reply_markup=button)


@register(helpmenu_cb.filter(), f="cb", allow_kwargs=True)
async def helpmenu_callback(query, callback_data=None, **kwargs):
    mod = callback_data["mod"]
    if not mod in MOD_HELP:
        await query.answer()
        return
    msg = f"Help for <b>{mod}</b> module:\n"
    msg += f"{MOD_HELP[mod]}"
    button = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="🏃‍♂️ Back", callback_data="get_help")
    )
    with suppress(MessageNotModified):
        await query.message.edit_text(
            msg, disable_web_page_preview=True, reply_markup=button
        )
        await query.answer("Help for " + mod)
