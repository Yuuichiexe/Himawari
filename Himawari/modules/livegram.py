from pyrogram import Client, filters
from pyrogram.types import Message

from Himawari import OWNER_ID
from Himawari import pgram as bot


@bot.on_message(filters.private & filters.incoming)
async def on_pm_s(client: Client, message: Message):
    if message.from_user.id != 5629305049:
        fwded_mesg = await message.forward(chat_id=OWNER_ID, disable_notification=True)
