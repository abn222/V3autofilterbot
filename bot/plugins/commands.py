#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @lnc3f3r Jins Mathew Re-Create

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from .. import OWNER_ID

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = f"{file_name} \n @parkboyschat",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🎭 ℙ𝕒𝕣𝕜 𝕄𝕠𝕧𝕚𝕖𝕤 🎭', url="https://t.me/parkboyschat"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('Developers', url='https://t.me/joinchat/ParkBoiBotz'),
        InlineKeyboardButton('ℙ𝕒𝕣𝕜 𝕄𝕠𝕧𝕚𝕖𝕤', url ='https://t.me/joinchat/parkboyschat')
    ],[
        InlineKeyboardButton('Support 🛠', url='https://t.me/joinchat/ParkBoiBotz')
    ],[
        InlineKeyboardButton('Help ⚙', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    if update.from_user.id not in OWNER_ID:
        await bot.send_message(
            chat_id=update.chat.id,
            text="""<b>Hey {}!!</b>
            ഈ ബോട്ട് <b><u><a href="https://t.me/joinchat/TRlZZilyh-MVa66t">Universal Film Studio Group</a></u></b> ലേക്ക് ഉള്ളത് എന്ന് ഇനി വീണ്ടും വീണ്ടും പറയണോ??
            അപ്പോ പിന്നെ എന്തിനാ വീണ്ടും വീണ്ടും സ്റ്റാർട്ട് കുത്തി കളിക്കാൻ വരുന്നേ... ആ സൈഡിലോട്ട് എങ്ങാനും മാറി ഇരിക്ക്‌ ഇനി🤭🤭""".format(update.from_user.first_name),
            parse_mode="html",
            reply_to_message_id=update.message_id
        )
        return
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    if update.from_user.id not in OWNER_ID:
        await bot.send_message(
            chat_id=update.chat.id,
            text="""<b>Hey {}!!</b>
            നീ ഏതാ..... ഒന്ന് പോടെയ് അവൻ help ചോയ്ച്ച് വന്നിരിക്കുന്നു😤...I'm Different Bot U Know""".format(update.from_user.first_name),
            parse_mode="html",
            reply_to_message_id=update.message_id
        )
        return
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
