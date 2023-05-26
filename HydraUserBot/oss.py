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
SESSION = "BQCbcXYABdg8LAU3QhlBPA1M2EaC6Cm-Y4R89anECwowgv24VF3mrl7xVbcGftiA5nGptigMJTMCGvoUIedx-XbNoLgXTVQreSevY9l3Kz52JqpK686Gi6B0KqK_kBr5e08I6aWmU4_dnbHO78Mx8lE0F9fsPzFit7Ob2kj98jyEzIuz2sFMAVxcbC1S_RqbXNNoqYeUEMwi7756z1nh_AGhDXjgVQ0Bp8UpZqmMuMBGwbgxBU3aro2xvlIJl5EjoL5tdrDPs5WpMVHZW4vKc9iLhAqKI-OLMOzSukRK2Xjsbou2dbF3G0kwYDt1nvCJv02LBrpuTeisNakNFGHcBM9MQTXcsAAAAAFji4RfAA"
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
