from HS1.HydraUserBot.oss import Hydra, bot

if __name__ == "__main__":
    Hydra.start()
    bot.run()
    with bot:
        bot.send_message("-1001859707851", "UB Ready")
