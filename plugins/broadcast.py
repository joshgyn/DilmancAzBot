from pyrogram import Client ,filters
import os
from helper.database import getid
ADMIN = int(os.environ.get("ADMIN", 5029360628))


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Bütün istifadəçilər data mərkəzindən çağırılır····>")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"Yayım başlanır ····> \n  {tot} İstifadəçiyə mesaj göndərilir ⏳")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass
