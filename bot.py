import telebot
BOT_TOKEN = "8968083032:AAGkh4e84sRxWzzFdhWKKhC-cMDGImuFDsY"
@bot.message_handler(commands=['start'])def start(message):bot.reply_to(message,"Hello!")
bot.infinity_polling()
