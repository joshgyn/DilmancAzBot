from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from helper.database import set,unset ,insert
from helper.list import list

@Client.on_message(filters.private &filters.command(['unset']))
async def unsetlg(client,message):
	unset(int(message.chat.id))
	await message.reply_text("Seçilmiş dil uğurla silindi 🤓")

@Client.on_message(filters.private &filters.command(['set']))
async def setlg(client,message):
    	    user_id = int(message.chat.id)
    	    insert(user_id)
    	    text = message.text
    	    textspit = text.split('/set')
    	    lg_code = textspit[1]
    	    if lg_code:
    	    		cd = lg_code.lower().replace(" ", "")
    	    		try:
    	    			lgcd = list[cd]
    	    		except:
    	    			await message.reply_text("❗️ Bu dil mənim seçimlərim arasında yoxdu 🤨 \n Düzgün yazdığına əminsən? 😉",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Dil kodları 📑" ,url="https://telegra.ph/Dil-kodları-02-18")]]))
    	    			return
    	    		set(user_id,lgcd)
    	    		await message.reply_text(f"Seçdiyin dil uğurla qeyd edildi **{cd}**")
    	    else:
    	    		await message.reply_text(" Zəhmət olmasa,qeyd etmək üçün 1 dil seç😑😑😑. \n **Məsələn:/set Azerbaijani**",reply_markup=InlineKeyboardMarkup([[	InlineKeyboardButton("Dil kodları 📑",url = "https://telegra.ph/Dil-kodları-02-18")]]))
