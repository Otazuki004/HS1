from pyrogram import filters

from HS1.config import HANDLER, OWNER_ID
from HS1.HydraUserBot.oss import Hydra


@Hydra.on_message(filters.command("join", prefixes=HANDLER) & filters.user(OWNER_ID))
def join_chat(_, m):
    if len(m.command) < 2:
        m.reply_text("ɢɪᴠᴇ ᴀ ᴊᴏɪɴ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪɴᴠɪᴛᴇ  ʟɪɴᴋ")
        return
    link = m.text.split(" ")[1]
    Hydra.join_chat(link)
    chat = Hydra.get_chat(link)
    name = chat.title
    m.reply_text(f"Successfully joined {name}")


@Hydra.on_message(filters.command("leave", prefixes=HANDLER) & filters.user(OWNER_ID))
def leave_chat(_, m):
    if len(m.command) < 2:
        m.reply_text("ɢɪᴠᴇ ᴀ ʟᴇғᴛ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪɴᴠɪᴛᴇ  ʟɪɴᴋ")
        return
    link = m.text.split(" ")[1]
    Hydra.leave_chat(link)
    chat = Hydra.get_chat(link)
    name = chat.title
    m.reply_text(f"Successfully left {name}")
