from pyrogram import filters

from HS1.config import HANDLER, OWNER_ID
from HS1.HydraUserBot.oss import Hydra


@Hydra.on_message(filters.command("spam2", prefixes=HANDLER) & filters.user(OWNER_ID))
async def write(_, message):
    if len(message.command) < 2:
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20"))
    )
    await Hydra.send_message(message.chat.id, f"name")
    await Hydra.send_message(message.chat.id, f"name")