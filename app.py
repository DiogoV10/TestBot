import re
from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name,URL


global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])

def respond():
   # retrieve the message in JSON and then transform it to Telegram object
   update = telegram.Update.de_json(request.get_json(force=True), bot)

   chat_id = update.effective_message.chat.id
   msg_id = update.effective_message.message_id

   # Telegram understands UTF-8, so encode text for unicode compatibility
   text = update.effective_message.text.encode('utf-8').decode()
   # for debugging purposes only
   print("got text message :", text)
   # the first time you chat with the bot AKA the welcoming message
   if text == "/start":
       # print the welcoming message
       bot_welcome = """
       Bem vindo! Digite /help caso precise de ajuda.
       """
       # send the welcoming message
       bot.sendMessage(chat_id=chat_id, text=bot_welcome)


   else:
       try:
           if text == "/allcommands":
                bot.sendMessage(chat_id=chat_id, text=
                "Aqui tens todos os comandos que pode utilizar:\n\n" +
                "/gitcomment\n" +
                "/wiki\n" +
                "/make\n" +
                "/projects\n" +
                "/gitbranches")

           if text == "/gitcomment":
                bot.sendMessage(chat_id=chat_id, text=
                "* feat(shopping cart): add the amazing button\n" +
                "* fix: add missing parameter to service call\n\n" +
                "  The error occurred because of <reasons>.\n\n" +
                "* build: release version 1.0.0\n" +
                "* build: update dependencies\n" +
                "* refactor: implement calculation method as recursion\n" +
                "* style: remove empty line\n" +
                "* revert: refactor: implement calculation method as recursion\n\n" +
                "  This reverts commit 221d3ec6ffeead67cee8c730c4a15cf8dc84897a.")

           if text == "/wiki":
                bot.sendMessage(chat_id=chat_id, text="https://caosdata.visualstudio.com/magiccupom-app/_wiki/wikis/magiccupom-app.wiki/2/Welcome-to-Magic-Cupom-APP")

           if text == "/make":
                bot.sendMessage(chat_id=chat_id, text=
                "'make setup' - creates all the environment for the project, usually this command is inside API module\n" +
                "'make destroy' - destroy the environment for the project, usually this command is inside API module\n" +
                "'make up' - turn on cluster, this command is usually available inside API module\n" +
                "'make down' - turn off cluster, this command is usually available inside API module\n" +
                "'make debug' - you can debug your module inside the cluster\n" +
                "'make cleanup' - clean your module if something is wrong\n" +
                "'make add_dep' - add dependencies into the project without the need of overwrite requirements file\n" +
                "'make rm_dep' - remove dependencies into the project without the need of overwrite requirements file\n" +
                "'make logs' - shows the server activity within 10 minutes\n" +
                "'make minikube_set_memory [memory]' - changes the amount of memory of your cluster")

           if text == "/projects":
                bot.sendMessage(chat_id=chat_id, text=
                "'gaia' - G.AI.A <https://caosdata.visualstudio.com/gaia-app>\n" +
                "'gaiabmg' - Gaia For BMG <https://caosdata.visualstudio.com/gaiabmg-app>\n" +
                "'magiccupom' - Magic Cupom <https://caosdata.visualstudio.com/magiccupom-app>\n" +
                "'scutaai' - Scuta.AI <https://caosdata.visualstudio.com/scutaai-app>")

           if text == "/gitbranches":
                bot.sendMessage(chat_id=chat_id, text=
                "You have to always create your branch from 'DEVELOP' branch\n\n" +
                "In https://sprints.zoho.com/ you can see your tasks\n" +
                "The name of your branch is the Card ID inside zoho\n\n" +
                "OBS: Your branch has to follow some guidelines\n\n" +
                "* If the card type is an issue or bug your branch has to be named as: issue/<card_id>\n" +
                "* If the card type is a task or story your branch has to be named as: feature/<card_id>\n" +
                "* remember that if your branch is a story, you can name it as the parent card id and make all the child tasks inside this branch")

           if text == "/help":
                bot.send_message(chat_id=chat_id, text=
                '1) Para receber uma lista dos comandos digite /allcommands.\n' +
                '2) Para ver se o bot está ativo digite /start.')

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