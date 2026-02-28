import telebot
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🤖 Bern Signal Pro Bot la ap mache! 🚀")

print("Bot la ap kouri...")
bot.infinity_polling()
