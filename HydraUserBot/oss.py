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


API_ID = "21660329"
API_HASH = "95c051dfc2888a2e79dc117de656e64d"
SESSION = "BQFKgqkAE-9f4GVika2-LY43HZfoOCLTBGFgwXZWCI8TBfSw7aSQv8Yr1iXQF-gLTrF1wdAcnhSFvtTLbgTv5OIIaUye-APBx9tkrlM0ckwG6eb8jQwiqAV2cfXad28pXDK1lqFiIMQw-MXCf1rGLKWiz-mRK8dUKGUuzSY5qbf9p2DQLE9M5SQTwfIvpoQ57vtlPc3eZD1DjX9FG38L0alXgFbXX2GnHKBgjE-Yta7FDobjqAcGk-GlTXRea8rEsGoikA4bsuN8qp5vAqv0NluogANYk5aPhUAFRUJs7Mma6VnN68m8C-xeHBfCcRgJANrF0EGv5hYlb09OUclLRfAXqenbkgAAAAFVXmQdAA"
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
