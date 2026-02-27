import telebot
import os

# Li token lan depi environment variable sou Render
TOKEN = os.environ.get("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TOKEN)

# Defini kòmand /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🤖 Bern Signal Pro Bot la ap mache! 🚀")

print("Bot la ap kouri...")
bot.infinity_polling()
