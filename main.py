from telebot import TeleBot
import chatBot

TOKEN = '5850797962:AAFukAKCIe7Cw2EcG2pczUkK_ZPr2DoRFRo'
bot = TeleBot(TOKEN)

help_message = \
    """ Я умею:
/help - расскажу, что я умею
/about - расскажу о себе
/portfolio - расскажу о своих достижениях за год
/contacts - расскажу как со мной связаться"""


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!'+ help_message)


@bot.message_handler(commands=['help'])
def bot_help(message):
    bot.send_message(message.chat.id, text=help_message)


@bot.message_handler(commands=['about'])
def bot_about(message):
    bot.send_message(message.chat.id, text=chatBot.about_message)


@bot.message_handler(commands=['portfolio'])
def bot_portfolio(message):
    bot.send_message(message.chat.id, text=chatBot.portfolio_message)


@bot.message_handler(commands=['contacts'])
def bot_contacts(message):
    bot.send_message(message.chat.id, text=chatBot.contacts_message)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, message.text)


bot.polling(none_stop=True, interval=0)
