import os

from pyrogram import filters
from requests import get

from HS1.config import HANDLER, OWNER_ID
from HS1.HydraUserBot.oss import Hydra


@Hydra.on_message(
    filters.user(OWNER_ID) & filters.command("git", prefixes=HANDLER)
)
async def git(_, message):
    if len(message.command) < 2:
        return await message.reply_text("give github username")
    user = message.text.split(None, 1)[1]
    res = get(f"https://api.github.com/users/{user}").json()
    data = f"""**Name**: {res['name']}
**UserName**: {res['login']}
**Link**: [{res['login']}]({res['html_url']})
**Bio**: {res['bio']}
**Company**: {res['company']}
**Blog**: {res['blog']}
**Location**: {res['location']}
**Public Repos**: {res['public_repos']}
**Followers**: {res['followers']}
**Following**: {res['following']}
**Acc Created**: {res['created_at']}
"""
    with open(f"{user}.jpg", "wb") as f:
        kek = get(res["avatar_url"]).content
        f.write(kek)

    await message.reply_photo(f"{user}.jpg", caption=data)
    os.remove(f"{user}.jpg")
