from datetime import datetime
from pytz import timezone
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config
from aiohttp import web
from route import web_server

ubot = Client(name="renameruser",
              api_id=Config.API_ID,
              api_hash=Config.API_HASH,
              sleep_threshold=15,
              no_updates=True,
              session_string="BQEYx1oAKm1n-4NIrKv6-NfbT5CfrlkqAqHskmI-7fmEWfuLYq1XvSv3urOFsTcX12Fgwv1KYIw9c1JNUtDCyihmIz4xHxNebaI0RXIsMjmSY2jXkCYu-n4GiX82YzpNK4T0RwozWg_TLy0DCrQpHOdhMvnqTER07I85c8VlyM9v8zl350c60XdJQtJp1SC93nj7GjdzlNwe6y3qCqU8KRUcxjnHJlCjtyZXUswDEQ7XqVKNR9tNmHrZ67iIQjZvchhxng-YfseZas6MqWuZSmszZYlt4yUq3ryF5CokQ9cia3XFYwpDOtWa_yWvUUgTSx6DE9RLjps-ZjYR92oqCPbU8MGHoAAAAAAo0B41AA",
              )


class Bot(Client):

    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username
        self.uptime = Config.BOT_UPTIME
        if Config.WEBHOOK:
            app = web.AppRunner(await web_server())
            await app.setup()
            await web.TCPSite(app, "0.0.0.0", 8080).start()
        print(f"{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️")
        for id in Config.ADMIN:
            try:
                await self.send_message(id, f"**__{me.first_name}  Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️__**")
            except:
                pass
        if Config.LOG_CHANNEL:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(Config.LOG_CHANNEL,
                                        f"**__{me.mention} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ !!**\n\n📅 Dᴀᴛᴇ : `{date}`\n⏰ Tɪᴍᴇ : `{time}`\n🌐 Tɪᴍᴇᴢᴏɴᴇ : `Asia/Kolkata`\n\n🉐 Vᴇʀsɪᴏɴ : `v{__version__} (Layer {layer})`</b>")
            except:
                print("Pʟᴇᴀꜱᴇ Mᴀᴋᴇ Tʜɪꜱ Iꜱ Aᴅᴍɪɴ Iɴ Yᴏᴜʀ Lᴏɢ Cʜᴀɴɴᴇʟ")
        await ubot.start()


Bot().run()
ubot.stop(True)
