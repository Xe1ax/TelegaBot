import telebot
from time import sleep
import random

bot = telebot.TeleBot('6863569903:AAF5-vYrLGR3uwVvVSdFL8ej4l9yHvjycqQ')

@bot.message_handler(commands = ['start'])
def start (message):
    bot.send_message(message.chat.id, 'Привет, я погодный бот, мои команды - short - для краткого прогноза погоды, long - для полного прогноза')
    
@bot.message_handler(commands = ['long'])
def long_prognoz (message):
    msg = bot.send_message(message.chat.id, "Предпочитаемый источник")
    bot.register_next_step_handler(msg, longIA)

@bot.message_handler(commands = ['short'])
def short_prognoz (message):
    pass

@bot.message_handler(content_types = ['text'])
def text(message):
    bot.send_message(message.chat.id, "Ты что-то хотел?")

bot.polling()
