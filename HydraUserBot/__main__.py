from HS1.HydraUserBot.oss import Hydra
import asyncio

if __name__ == "__main__":
    Hydra.start()
    Hydra.run_until_disconnected()
