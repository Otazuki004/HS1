from HS1.HydraUserBot.oss import Hydra
import asyncio

if __name__ == "__main__":
    Hydra.start()
    await Hydra.run_until_disconnected()
