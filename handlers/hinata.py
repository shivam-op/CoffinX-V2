from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAADBAADJgMAAqKYZgAB0UH2shlpMSsC", "CAADBAADLAMAAqKYZgABayywIAiqZ0gC", "CAADBAADOAMAAqKYZgABh5wcd4QnpcwC", "CAADBAADPQMAAqKYZgABur46JrhDohYC", "CAADBAADswMAAqKYZgABVzxxH4lMba0C", "CAADBAAD3gQAAqKYZgABmxmc1Y3A4xQC", "CAADBAADWAUAAqKYZgAB1ia7fuNxpq4C", "CAADBAADXA4AAh3PuAc4x8-E_-7aygI", "CAADBAADeg4AAh3PuAe2kQ3GPRO3hwI", "CAADBAADkg4AAh3PuAcj4B3CTwjDiQI", "CAADBAADiwIAAsiLDQhiubnq7ueZrgI", "CAADBAADmQIAAsiLDQgLP7VMIuZXgAI", "CAADBAADmwIAAsiLDQiPkeWZT0jKPQI", "CAADBAADlQIAAsiLDQhcIu-tSCjcBQI", "CAADBAADjwIAAsiLDQjYx7KvqxKFMgI", "CAADBAADnwIAAsiLDQibN_CcD5zfkQI", "CAADBAADnQIAAsiLDQihvo41EnrDzAI", "CAADBAADpQIAAsiLDQjK923PGHm5QQI", "CAADBAADowIAAsiLDQgvfkwYeEQ-2QI", "CAADBAADpwIAAsiLDQizmtsoKxTPggI", "CAADBAADrQIAAsiLDQgMCsrjsg3v4wI", "CAADBAADrwIAAsiLDQjIXFtjd_TqNAI", "CAADBAADtwIAAsiLDQiBcvZcIdSJGgI", "CAADBAADsQIAAsiLDQhLpnmM589abAI", "CAADBAAD0QIAAsiLDQhh8fBJJVLT8QI", "CAADBAAD0wIAAsiLDQgkmlDTS1nm7QI", "CAADBAAD1wIAAsiLDQgNRH763A4EjgI", "CAADAQADoQEAArna9gmuB8gVICvS9wI", "CAADAQADqQEAArna9gnqCzMdDF0lUAI", "CAADAQADrQEAArna9glHGcsWYKiMRAI", "CAADAQADqwEAArna9gkmp05lNiNn9wI", "CAADAQADtwEAArna9gkDeV746IbSwQI", "CAADAQADvQEAArna9gnuMPtOZrW1PQI", "CAADAQADvwEAArna9glCn8R5s1LbZAI", "CAADBAADJgEAAqM2qAemZ_YJbuzDJwI", "CAADBAADOQEAAqM2qAfkrc477ntjIgI", "CAADBAADMAEAAqM2qAeX7j7nLeiNFQI", "CAADBAADVAEAAqM2qAd0tDCJZ3A8ggI", "CAADBAADUQEAAqM2qAdbGe9WG9EogQI", "CAADBAADTAEAAqM2qAd-3A6X_ijf1wI", "CAADBAADSAEAAqM2qAcAAUws3DcwQdIC", "CAADBAADRgEAAqM2qAdssyA7IPhymQI", "CAADBAADVgEAAqM2qAeDuMRxavg-9gI", "CAADBAADhAADDvcmBlTiJw2iW3-DAg", "CAADBAADhgADDvcmBhTDcsXEcO8RAg", "CAADBAADiAADDvcmBmtco0ch3eYmAg", "CAADBAADigADDvcmBsN4in4FXW4aAg", "CAADBAADoQADDvcmBn7hBgmWUK1xAg", "CAADBAADrQADDvcmBpQJ1c4eo8SaAg", "CAADBAADxQQAAsOSbAP7HMKduOaRDAI", "CAADBAAD0QQAAsOSbAPzeE-N7Wo1XAI", "CAADBAAD1wQAAsOSbAMUAabgPzSUxAI", "CAADBAAD2QQAAsOSbAM5-ZiM9NwCYQI", "CAADBAAD3wQAAsOSbAN8cWh9AAGZ4JEC", "CAADBAAD7QQAAsOSbAP87mq-1IhdVAI", "CAADBAADngUAAsOSbAPyZJxHHwABDOsC", "CAADBAADuwUAAsOSbAPVCu6yVd9AYgI", "CAADBAADTwEAAqIkSQOcLYaijPdA9AI", "CAADBAADewEAAqIkSQOKtlOA7PDVswI", "CAADBAADfwEAAqIkSQMwmItrQLEAAbQC", "CAADBAADigEAAqIkSQNNtoHkx9ztAQI", "CAADBAADkAEAAqIkSQMLvYm2Z-WYYgI", "CAADBAADmAEAAqIkSQP6IpIzeuoqdQI", "CAADBAADmgEAAqIkSQPznG-Ig4iwAQI", "CAADBAADogEAAqIkSQMs3FfHKdWVzAI", "CAADBAADqAEAAqIkSQPH-RWOk7OuDQI", "CAADBAADtgEAAqIkSQNaxXsO6qI36gI", "CAADBAADvwEAAqIkSQOeSXUAAS1PnwsC", "CAADBAAD8AEAAqIkSQOYAAF3LuxtgicC", "CAADBAAD_AEAAqIkSQNHqmcGA9vgeAI", "CAADBAAD8gEAAqIkSQMqnIXPK9AO4AI", "CAADBAAD-AEAAqIkSQOST8xeeqZZ_QI", "CAADBAADyAUAAuAFHALE9DV1idj8GQI", "CAADBAAD0AUAAuAFHAKKqQlswE-TxAI", "CAADBAAD7gUAAuAFHAJt4SYHShUyHQI", "CAADBAAD1gUAAuAFHALWRdze8hSGgAI", "CAADBQADYgAD6NvJAjw6mwsi3ZDcAg", "CAADBQADawAD6NvJAvSDRGZiKm0-Ag", "CAADBAADawYAApesNQABqnPuHOSm_rUC", "CAADBAADggYAApesNQABY52p_5jYmDAC", "CAADBAADkgYAApesNQABrWxxAo4i5YIC", "CAADBAADlgYAApesNQABAaQoqR18rJcC", "CAADBAADwAYAApesNQABj-Un4Rf2kAEC", "CAADBAADpgMAApv7sgABKyxNf3LVHeAC", "CAADBAADtAMAApv7sgAB-1esnD-WlHIC", "CAADBAAD7gMAApv7sgABGCZKqVeej3YC", "CAADAwADhAAD_ZPKAAGphJ9IUmjqqAI", "CAADAgADsgADdqy6ButIWEMMsnSMAg", "CAADAQADygMAAuJbQAVEJd8sOLqNJwI", "CAADAQADyAMAAuJbQAU-y13TznSWXwI", "CAADAQAD1AMAAuJbQAXPlcSmhmgxOgI", "CAADBAADfQADylycBfFLFOlpUkSAAg", "CAADBAADfwADylycBerATexgP5rfAg", "CAADBAADgQADylycBRxpx-hgT8dBAg", "CAADBAADgwADylycBapS4Fz1ozG4Ag", "CAADBAADhwADylycBUXx92Qbc0HeAg", "CAADBAADogADylycBWLXUovOwXa6Ag", "CAADBAAD3gADylycBS0QiC-O4zvYAg", "CAADBAADDAUAAspcnAU4aO3nT9quMAI", "CAADBAADHgUAAspcnAVLCx1VIZ2laQI", "CAADBAADOAUAAspcnAV7Wx41DCZINwI", "CAADBAADaQEAAl7ugQYqaKHrgmb7mgI", "CAADBAADOQQAAnZY-wJXL61k-or-uwI", "CAADBAADQgQAAnZY-wJ2XZvSz11GhQI", "CAADBAADTgQAAnZY-wK6b_dynGPoTAI", "CAADBAADlwMAAspcnAWOVBRIBv3K7QI", "CAADBAADmwMAAspcnAVYLJLwdXI4twI", "CAADBAADvwMAAspcnAXh31MvOjw4_wI", "CAADBAAD-QMAAspcnAU7QO_IByh3UQI", "CAADBAAD5QMAAspcnAW5Pl-29Mre9gI", "CAADBAADBwQAAspcnAUaKvx4Bb99kQI", "CAADBAADQwQAAspcnAW3qRleNi9aNQI", "CAADBAADxQwAAuf7rQZlyZi2n5t29QI", "CAADBAADzwwAAuf7rQZMLO8dV3dzTAI", "CAADBAAD1wwAAuf7rQZvaEDPm8950gI", "CAADBAAD0wwAAuf7rQZat80CHwABEtcC", "CAADBAAD0QwAAuf7rQa1vDSzF2iXDAI", "CAADBAAD3wwAAuf7rQYE4k-pmuUnIQI", "CAADBAADYA0AAuf7rQabM1fOJ2yZ1wI", "CAADBAADYw4AAuf7rQYZUvpBdCk2pgI", "CAADBAADhg4AAuf7rQbJl5Bat1xMsgI", "CAADBAADiA4AAuf7rQb2C3BKd6Z8pgI", "CAADBAADZg4AAuf7rQbJ4vrW-y-CPAI", "CAADBQADKhgAAsZRxhWrNMZW8VO5PwI", "CAADBQAD_RgAAsZRxhXU78dx1KWHswI", "CAADBQADqBkAAsZRxhUZNMbd9XQk8gI", "CAADBQADExIAAsZRxhVgT_7AMtFGlwI", "CAADBQADyQ4AAsZRxhULL8-YqNW8hgI")
    await message.reply_text(
        f"""<b>Hey!! {message.user.mention} 
\nI'm Here to Play music In your voice chat...
maintain by @CoffinXSupport..✨
\nuse this inline buttons to know more 😉😉.
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🚑 Support group 🚑", url="t.me/CoffinXsupport")
                  ],[
                    InlineKeyboardButton(
                        "ℹ️ updates channel", url="https://t.me/CoffinX_updates"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 Creator 👨‍💻", url="https://t.me/xD_shashank"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "💁 Assistant 💁", url="https://t.me/CoffinXPlayer"
                    )],
                    [ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/CoffinXmusic_bot?startgroup=true"
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
                        "🚑 SUPPORT GROUP 🚑", url="https://t.me/CoffinXsupport")
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
            
@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n❖ /play <song name> - play song you requested
❖ /dplay <song name> - play song you requested via deezer
❖ /splay <song name> - play song you requested via jio saavn
❖ /playlist - Show now playing list
❖ /current - Show now playing
❖/song <song name> - download songs you want quickly
❖ /search <query> - search videos on youtube with details
❖ /deezer <song name> - download songs you want quickly via deezer
❖ /saavn <song name> - download songs you want quickly via saavn
❖ /video <song name> - download videos you want quickly
\n*Admins only*
✪ /player - open music player settings panel
✪ /pause - pause song play
✪ /resume - resume song play
✪ /skip - play next song
✪ /end - stop music play
✪ /userbotjoin - invite assistant to your chat
✪ /admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/CoffinX_updates"
                    ),
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/CoffinXsupport"
                    )
                ]
            ]
        )
    )                
