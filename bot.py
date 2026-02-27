Python
Copier le code
import telebot

# Mete token ou jwenn nan BotFather isit
TOKEN = "VOTRE_TOKEN_LAN"

bot = telebot.TeleBot(TOKEN)

# Reponn lè moun tape /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🤖 Bern Signal Pro Bot la ap mache!")

# Ou ka ajoute plis fonksyonalite isit la
# Egzanp: voye siyal, mesaj otomatik, etc.

print("Bot la ap kouri...")
bot.infinity_polling()
