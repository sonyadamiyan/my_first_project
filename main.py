import telebot

token='6782274357:AAH2lzs9kLCVqe9gGXg2g_H9LzkfWPNMnXQ'
bot=telebot.TeleBot(token)

def filter_password(message):
    password = "хомяк"
    return password in message.text

@bot.message_handler(content_types=['text'], func = filter_password)
def say_hello(message):
    bot.send_message(message.chat.id, "Привет!")

bot.polling()
