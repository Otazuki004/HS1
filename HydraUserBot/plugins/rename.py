import os

from pyrogram import filters

from HS1.config import HANDLER, OWNER_ID
from HS1.HydraUserBot.__init__ import Hydra


@Hydra.on_message(filters.command("rename", prefixes=HANDLER) & filters.user(OWNER_ID))
def rename(_, message):

    try:
        filename = message.text.replace(message.text.split(" ")[0], "")

    except Exception as e:
        print(e)

    if reply := message.reply_to_message:
        x = message.reply_text("Downloading.....")
        path = reply.download(file_name=filename)
        x.edit("Uploading.....")
        message.reply_document(path)
        os.remove(path)
