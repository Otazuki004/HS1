from HS1.HydraUserBot.oss import Hydra as bot
from pyrogram import filters

@bot.on_message(filters.command("kick") & filters.user(5965055071)) 
def ban(bot, message):
	bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
	bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
	bot.send_message(message.chat.id, f"Successfully Kicked! {message.reply_to_message.from_user.mention}.")
	
	
@bot.on_message(filters.command("ban") & filters.user(5965055071)) 
def ban(bot, message):
	bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
	bot.send_message(message.chat.id, f"Successfully Banned") 

	
	

