from HS1.HydraUserBot.oss import Hydra
import asyncio

if __name__ == "__main__":
    Hydra.start()
    asyncio.get_event_loop().run_until_complete(main(Hydra))
