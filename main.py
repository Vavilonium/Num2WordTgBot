import telebot

from NumbersToWords import *
import config

bot = telebot.TeleBot(config.Token)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте! Введите число от 1 до 9999.")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Просто введите число от 1 до 9999")


@bot.message_handler(content_types=['text'])
def Convert(message):
    try:
        number = int(message.text)
        if not 1 <= number <= 9999:
            bot.send_message(message.chat.id, "Ваше число не в диапазоне, введите число от 1 до 9999")
        else:
            msg2usr = (number_to_words(number).capitalize(), sklonenie(number))
            bot.send_message(message.chat.id, deletecharacters(str(msg2usr)))

    except ValueError:
        bot.send_message(message.chat.id, "Это не число!")


bot.polling(none_stop=True)
