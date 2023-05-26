import logging
import os
import time

from aiohttp import ClientSession
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
SESSION = "BQCPdzzCClQ7zm4l6Zm8ozar2G2kqUbjZfjRRzfsBZSZVvVGy8BRHeIyphdibmtA8hyKTG14RmEu5Gbr_i7NlGy3cSowd2zYfh79ApOWSu49kSHcc6sAt1IR8J6zmjXD36qcbt5Utd_B-1G2Kq2aI_LyCKyVakhSEkLs_ZZXqzaw4vi6Drnpaykpg7xTInxo9IRYvseRi1xst6TGZ2Q62JAA4nsriJZQb-hROq66eckSO9gSiDPihcQXpOVCZfp2ZE6Cch9e9ImW7YUmr2gRTQthtSTv4jPuHKwakDFBmm5YjAKmF72ntp7pYmzbYD5g8EYMwpXjC2MrdMsnFQO-aBAAAAAWOLhF8A"
BOT_TOKEN = "5928285583:AAEK8qamRXuajFrZP3pFOMti-r4VOQ4uhaM"

# install aiohttp session
print("[HYDRAUSERBOT] Initializing AIOHTTP Session")
aiohttpsession = ClientSession()


bot = Client(
    "HydraUserBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="{}/plugins".format(__name__)),
)
Hydra = Client(session_string=SESSION, api_id=API_ID, api_hash=API_HASH, name="Hydra")
