from HS1.config import LOG_GROUP_ID
from HS1.HydraUserBot.oss import bot, Hydra

if __name__ == "__main__":
    main()
    Hydra.start()
    bot.run()
    with bot:
        bot.send_message(f"{LOG_GROUP_ID}", "UB Ready")
