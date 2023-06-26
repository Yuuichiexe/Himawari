from telethon import Button

from Himawari import tbot
from Himawari.events import register

PHOTO = "https://graph.org/file/c8800bdf565ea841d87ee.mp4"


@register(pattern=("Good night"))
async def awake(event):
    MEOW = f"Gᴏᴏᴅ  ɴɪɢʜᴛ 🥀 ɪ ʜᴏᴘᴇ  ᴛᴏᴍᴏʀʀᴏᴡ ɪꜱ ᴛʜᴇ ʙᴇꜱᴛ  ᴅᴀʏ ɪɴ ʏᴏᴜʀ ʟɪꜰᴇ. {event.sender.first_name}"
    BUTTON = [
        [
            Button.url("Mᴇᴇᴛ ᴍᴇ Hᴇʀᴇ ✨", "https://telegram.dog/xtromxsupport"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=NEKO, buttons=BUTTON)
