import re
from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name,URL


global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.reply_to(message, "Hello, welcome to Telegram Bot!")
    
# handle all messages, echo response back to users
@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
	bot.reply_to(message, message.text)


bot.polling()