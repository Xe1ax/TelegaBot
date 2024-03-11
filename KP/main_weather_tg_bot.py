import datetime
import requests
from config import tg_bot_token, open_weather_token
import telebot

bot = telebot.TeleBot(tg_bot_token)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Напиши мне название города и я пришлю сводку погоды!")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric&lang=ru"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        general_forecast = data["weather"][0]["description"]

        bot.send_message(message.chat.id, f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                            f"Погода в городе: {city}\nТемпература: {cur_weather}C°\nОщущается как: {feels_like}C°\n"
                            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/c\n"
                            f"Общий прогноз: {general_forecast}")

    except Exception as e:
        bot.send_message(message.chat.id, "\U00002620 Проверьте название города \U00002620")

bot.infinity_polling()
