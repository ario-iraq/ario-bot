from pyrogram import Client, filters

@Client.on_message(filters.command("هلو") & filters.private)
async def hello(client, message):
    await message.reply("هلو عباس، شلونك؟")
