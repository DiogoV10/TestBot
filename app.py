import re
from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name,URL
import telebot


global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])

def respond():
   # retrieve the message in JSON and then transform it to Telegram object
   update = telegram.Update.de_json(request.get_json(force=True), bot)

   chat_id = update.message.chat.id
   msg_id = update.message.message_id

   # Telegram understands UTF-8, so encode text for unicode compatibility
   text = update.message.text.encode('utf-8').decode()
   # for debugging purposes only
   print("got text message :", text)
   # the first time you chat with the bot AKA the welcoming message
   if text == "/start":
       # print the welcoming message
       bot_welcome = """
       No.
       """
       # send the welcoming message
       bot.sendMessage(chat_id=chat_id, text=bot_welcome)


   else:
       try:
           if text == "/echo":
                bot.sendMessage(chat_id=chat_id, text="Do /echo [text]")
           elif text.startswith("/echo "):  
                user = text[6:]
                bot.sendMessage(chat_id=chat_id, text=user)

           if text == "/greet":
                markup = telebot.types.InlineKeyboardMarkup()
                markup.add(telebot.types.InlineKeyboardButton(text='Bom dia', callback_data=1))
                markup.add(telebot.types.InlineKeyboardButton(text='Boa tarde', callback_data=2))
                markup.add(telebot.types.InlineKeyboardButton(text='Boa noite', callback_data=3))

                bot.send_message(chat_id=chat_id, text="Choose your greeting:", reply_markup=markup)

                bot.answer_callback_query(callback_query_id=call.id, text='Answer accepted!')
                answer = 'You made a mistake'
                if call.data == '1':
                    answer = 'Bom dia!'

                bot.send_message(chat_id=chat_id, answer)
                bot.edit_message_reply_markup(chat_id=chat_id, call.message.message_id)

           if text == "/commands":
                bot.sendMessage(chat_id=chat_id, text="Commands: /echo; /greet; /help")

           if text == "/help":
                bot.send_message(chat_id=chat_id, text=
                '1) To receive a list of available currencies press /exchange.\n' +
                '2) Click on the currency you are interested in.\n' +
                '3) You will receive a message containing information regarding the source and the target currencies, ' +
                'buying rates and selling rates.\n' +
                '4) Click “Update” to receive the current information regarding the request. ' +
                'The bot will also show the difference between the previous and the current exchange rates.\n' +
                '5) The bot supports inline. Type @<botusername> in any chat and the first letters of a currency.')

       except Exception:
           # if things went wrong
           bot.sendMessage(chat_id=chat_id, text="There was a problem in the name you used, please enter different name", reply_to_message_id=msg_id)

   return 'ok'

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