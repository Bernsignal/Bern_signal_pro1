import telebot
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🚀 Ynerlio Signal Bot aktif! Pare pou voye siyal 🔥")

print("Bot la ap kouri...")
bot.infinity_polling()
