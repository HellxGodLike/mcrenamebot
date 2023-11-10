"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

import re, os, time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "18401114")
    API_HASH = os.environ.get("API_HASH", "e9105cffc9ef49b4011dfeb843acb091")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5976019173:AAHjBxoQJ5PbZRHOzOA4CXkduhE2P3T2TU8")

    # database config
    DB_NAME = os.environ.get("DB_NAME", "pyro-botz")
    DB_URL = os.environ.get("DB_URL",
                            "mongodb+srv://speedrenamebot:speedrenamebot@cluster0.iiud8lq.mongodb.net/?retryWrites=true&w=majority")

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/b28df58e420e1e71c044a.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in
             os.environ.get('ADMIN', '684727861').split()]
    FORCE_SUB = os.environ.get("FORCE_SUB", "-1001864105634")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", None))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hᴀɪ {} 👋,
ɪ ᴀᴍ ᴀ ꜱɪᴍᴩʟᴇ 2ɢʙ ꜰɪʟᴇ ʀᴇɴᴀᴍᴇ+ꜰɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ ᴄᴏɴᴠᴇɴᴛᴏʀ ʙᴏᴛ
ᴡɪᴛʜ ᴛʜᴜᴍʙɴᴀɪʟ & ᴄᴜꜱᴛᴏᴍ ᴄᴀᴩᴛɪᴏɴ ꜱᴜᴩᴩᴏʀᴛ🗿
ᴛʜɪꜱ ʙᴏᴛ ᴡᴀꜱ ᴄʀᴇᴀᴛᴇᴅ ʙʏ : @Mc_adzz</b>"""

    ABOUT_TXT = """<b>╭━━❰ 𝗦𝗣𝗘𝗘𝗗 𝗥𝗘𝗡𝗔𝗠𝗘 𝗕𝗢𝗧 ❱━━━➣
┣⪼🤖 ᴍy ɴᴀᴍᴇ : {}
┣⪼🖥️ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : <a href=https://t.me/mc_adzz>𝗠𝗖 𝗔𝗗𝗭𝗭</a> 
┣⪼📕 Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
┣⪼✏️ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
┣⪼💾 Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>     
╰━━━━━━━━━━━━━━━━━━━━━━━➣ """

    HELP_TXT = """
🌌 <b><u>ʜᴏᴡ ᴛᴏ ꜱᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ</u></b>
  
<b>•»</b> /start Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•»</b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•»</b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.
📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>
<b>•»</b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•»</b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•»</b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
Exᴀᴍᴩʟᴇ:- /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}
✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•»</b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nɴᴀᴍᴇ \nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           
ℹ️ 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/moviecomplexadminbot>𝗔𝗗𝗠𝗜𝗡</a>
"""

    # ⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @ᴩyʀᴏ_ʙᴏᴛᴢ🙏🥲
    DEV_TXT = """<b><u>𝗠𝗖 𝗔𝗗𝗭𝗭</b></u>
» 𝗠𝗖 𝗔𝗗𝗭𝗭 : <a href=https://telegram.me/mc_adzz>𝗨𝗣𝗗𝗔𝗧𝗘𝗦</a>
» 𝗠𝗖 𝗚𝗥𝗢𝗨𝗣 : <a href=https://telegram.me/moviecomplexofficialgroup>𝗠𝗢𝗩𝗜𝗘 𝗖𝗢𝗠𝗣𝗟𝗘𝗫 𝗚𝗥𝗢𝗨𝗣</a>"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""
