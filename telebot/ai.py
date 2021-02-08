def start(bot,update):
    name  = update.message.from_user.first_name  #first name of the user messaging
    reply = "Hi!! {}".format(name)
    bot.send_message(chat_id = update.message.chat_id, text = reply)      #sending message

def help(bot,update):
    reply = "How can I help You"
    bot.send_message(chat_id = update.message.chat_id, text = reply)  #sending message

def echo_text(bot,update):
    reply = update.message.text
    bot.send_message(chat_id = update.message.chat_id, text = reply)

def sticker(bot,update):
    reply = update.message.sticker.file_id
    bot.send_sticker(chat_id = update.message.chat_id, sticker = reply)

def error(bot,update):
    logger.error("Shit!! Update {} caused error {}".format(update,update.error))