from pyrogram import Client, filters
from config import BOT_TOKEN, API_ID, API_HASH
import plugins

app = Client("ario", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("بوت آريو شغال.")

app.run()
