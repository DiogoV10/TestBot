def echo(text):
    while text != "/stop":
        bot.sendMessage(chat_id=chat_id, text=text)