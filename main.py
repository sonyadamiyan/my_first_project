from telebot import TeleBot
import chatBot
bot = TeleBot('5850797962:AAFukAKCIe7Cw2EcG2pczUkK_ZPr2DoRFRo')

help_massange = \
    """ Я умею:
/help - помогу, расскажу что умею
/about - расскажу о себе"""


@bot.message_handlers(commands=['start'])
def bot_start(message):
    bot.send_message(message.chat.id,
                     text=f"Привет, {message.from_user.first_name}" + help_massange)


@bot.message_handler(commands=['help'])
def bot_help(message):
    bot.send_message(message.chat.id, text=help_massange)


@bot.message_handlers(commands=['about'])
def bot_about(message):
    bot.send_message(message.chat.id, text=chatBot.about_me)


bot.polling()

