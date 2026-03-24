import os, telebot
from flask import Flask
import threading

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot aktif"

def run():
    app.run(host="0.0.0.0", port=10000)

threading.Thread(target=run).start()
bot.polling()
