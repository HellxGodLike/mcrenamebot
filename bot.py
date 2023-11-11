from datetime import datetime
from pytz import timezone
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config
from aiohttp import web
from route import web_server

ubot = Client(name="renameruser",
              api_id=18401114,
              api_hash="e9105cffc9ef49b4011dfeb843acb091",
              sleep_threshold=15,
              no_updates=True,
              session_string="BQEYx1oAiLn_pZXInt3wQuCF24IlzkypyHhWhatNZ0xDaDh6FahQbfW5Y_IXW6pIfiyyPXchKaelbmz7byr4RVzjEvC1hoHxBMTVo4Kh1Z2h6ASzHS9U33D27LDi68oaVv2I2AvlGSP548uSLoaZnuENRzv2z4i4pFz1bCi6pXtiF4rBr9BLc8FfLJ637JHBCbGPvxE3lpucnh0EPPq4c78iXJceDKrKlfK9dDlF5YjWjpXnjyLpq7a1d1Vx0MLeGZQwORv53dGtQvf7fU2FI8FcRNgqWZlwiNqyQCaQ-JcpdeJuPn0EOJ3AAgfC1c7EZA1EkwVb3zr3YtWdqsLizUCDum9cNgAAAAAo0B41AA",
              )

Bot = Client(name="renamer",
             api_id=Config.API_ID,
             api_hash=Config.API_HASH,
             bot_token=Config.BOT_TOKEN,
             workers=200,
             plugins={"root": "plugins"},
             sleep_threshold=15,
             )


async def mainrun():
    await Bot.start()
    await ubot.start()
    # if Config.WEBHOOK:
    #    app = web.AppRunner(await web_server())
    #   await app.setup()
    #   await web.TCPSite(app, "0.0.0.0", 8080).start()
    print(f"{Bot.me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️")
    for id in Config.ADMIN:
        try:
            await Bot.send_message(id, f"**__{Bot.me.first_name}  Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️__**")
        except:
            pass
    if Config.LOG_CHANNEL:
        try:
            curr = datetime.now(timezone("Asia/Kolkata"))
            date = curr.strftime('%d %B, %Y')
            time = curr.strftime('%I:%M:%S %p')
            await Bot.send_message(Config.LOG_CHANNEL,
                                   f"**__{Bot.me.mention} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ !!**\n\n📅 Dᴀᴛᴇ : `{date}`\n⏰ Tɪᴍᴇ : `{time}`\n🌐 Tɪᴍᴇᴢᴏɴᴇ : `Asia/Kolkata`\n\n🉐 Vᴇʀsɪᴏɴ : `v{__version__} (Layer {layer})`</b>")
        except:
            print("Pʟᴇᴀꜱᴇ Mᴀᴋᴇ Tʜɪꜱ Iꜱ Aᴅᴍɪɴ Iɴ Yᴏᴜʀ Lᴏɢ Cʜᴀɴɴᴇʟ")
    await ubot.stop(True)
    await Bot.stop(True)


if __name__ == "__main__":
    Bot.run(mainrun())
