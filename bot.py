from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "5168917169:AAERVOdGsI6TV6WegaNj794YpWNXa4XCfco")

API_ID = int(os.environ.get("API_ID",5866979))

API_HASH = os.environ.get("API_HASH", "9182938d2e0eaac257c3a563ab0877a9")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "GTBot",
        bot_token=TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
    )
    app.run()
