import telebot

token='5850797962:AAFukAKCIe7Cw2EcG2pczUkK_ZPr2DoRFRo'
bot=telebot.TeleBot(token)

def filter_password(message):
    password = "хомяк"
    return password in message.text

@bot.message_handler(content_types=['text'], func = filter_password)
def say_hello(message):
    bot.send_message(message.chat.id, "Привет!")

bot.polling()
