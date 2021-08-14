#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>SMILE KILLER</a>\n○ GROUP :  <a href='https://t.me/FILMCORNERMM/'>CLICK HERE</a>\n○ GROUP : <a href='https://t.me/NAZRIYAOFFTOPIC/'>CLICK HERE</a>\n○ CHANNEL : <a href='https://t.me/FILM_CORNER_OFFICIAL/'>CLICK HERE</a>\n○ CHANNAL : <a href='https://t.me/NAZRIYAONTOPIC/'>CLICK HERE</a>\n○ GROUP : <a href='https://t.me/NAZRIYASUPPORT/'>CLICK HERE</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
