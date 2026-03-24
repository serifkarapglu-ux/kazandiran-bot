import os
import telebot
from flask import Flask
import threading

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot aktif"

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "Merhaba! Bot çalışıyor ✅\nSatın almak için /satınal yaz")

@bot.message_handler(commands=['satınal'])
def satınal(msg):
    bot.reply_to(msg, "Ürün 49₺\nÖdeme linki: https://iyzico.com/xxxx\nÖdeme yaptıktan sonra 'ödendi' yaz")

def run():
    app.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    threading.Thread(target=run).start()
    bot.polling(none_stop=True)
