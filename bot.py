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
              session_string="BQEYx1oANVHw5IW1iyTNagH_jWQ6SJis1Xehx-YraxhdPvqmNBgN8gVg8I-W4e9WiZFr4-xzHnDhqhmMw1tb95PgCJWPSO_KLHnp0Xu3BHV9WCgnLQg8SEKV3LsQKQuycOsjTbb46f1XyhqMmz63228wuWppzdLkIsconnafIMCSVhgvGfI7GIURxT7FdxAalXdf_8dTrk0wdzvxLzeJsmsOwaj5_9OQmwMYBFv14XXi92Rt55vHk1b6PAMdB3bF2wOSds4woDX72jKs6Rpssi40qnyMx_cf75Oa9_pE0Uxt2WWw1SKkGgiKEW5EPXkleQL7qllUD8dYes4CsPpEo788irTG2gAAAAAo0B41AA",
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


ubot.start()
Bot().run()
ubot.stop(True)
