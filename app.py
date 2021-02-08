import re
from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name,URL


global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)



def main():
    updater = Updater(TOKEN)  #take the updates
    dp = updater.dispatcher   #handle the updates

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo_text))   #if the user sends text
    dp.add_handler(MessageHandler(Filters.sticker, sticker))  #if the user sends sticker
    dp.add_error_handler(error)
    updater.start_polling()
    logger.info("Started...")
    updater.idle()


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
   s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
   if s:
       return "webhook setup ok"
   else:
       return "webhook setup failed"

@app.route('/')
def index():
   return '.'


if __name__ == '__main__':
   app.run(threaded=True)
   main()