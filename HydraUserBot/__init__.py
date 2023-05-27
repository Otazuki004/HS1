import logging
import os
import time
from pyrogram import Client
# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
# bot =  [uptime,starttime,endtime]
StartTime = time.time()
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time
API_ID = "10187126"
API_HASH = "ff197c0d23d7fe54c89b44ed092c1752"
SESSION = "BQAIzBI_8PgN53GlEpzUHAABYZwmnJFbP4d_EoKrHAOomhZNmCKY6LDre_rn2hsFvz9GlXf9fBhyIeODeuRyDkcraxfV7HBkrd4pMs-HldbsCgmhX5I31_UGkS8sBK-iEAC8NrpCUV-fYb7yaUV_UlANJc5FQWxXT-n47gWrcz-lege4pTE4-FcJbmcQVeElqgoNPHCLdgBFpBJWUb2SwMR-RefhLNDVujjFLCDfWO4g7tOdqpfmPfMu-wiaIygeECLPCU2l7l8VpSYbWxzMCgZlOxBZinQpMGhfi4XfTZxR3h4H2L5qyZPWTndv8uyCO7o_ZRmgxYCMgGclHLQpwLz1AAAAAWOLhF8A"
BOT_TOKEN = "5928285583:AAEK8qamRXuajFrZP3pFOMti-r4VOQ4uhaM"
# install aiohttp session
print("[HYDRAUSERBOT] Initializing AIOHTTP Session")
bot = Client(
    "HydraUserBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="{}/plugins".format(__name__)),
)
Hydra = Client(session_string=SESSION, api_id=API_ID, api_hash=API_HASH, name="Hydra")