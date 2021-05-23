# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyowm
import telebot
from pyowm.utils.config import get_default_config


bot = telebot.TeleBot("1802555647:AAGV-mNEgc92GxLT2Dlgd2C0PM9MctCGlI8")
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM('1690d76ad190b1a89bf446288d3ad850', config_dict)
@bot.message_handler(content_types=["text"])

def telegrambot(message):
    if message.text == "/start" or message.text == "/help":
        bot.send_message(message.chat.id, "Привет! Напиши мне название города на английском и я расскажу тебе о погоде")
    else:
        mgr = owm.weather_manager()
        try:
            observation = mgr.weather_at_place(message.text)
        except:
            bot.send_message(message.chat.id, "Извините, я не знаю такого города :(\nПопробуйте еще раз")
            return
        w = observation.weather
        reg = owm.city_id_registry()
        loc = reg.locations_for(message.text)
        town = loc[0]
        one_call = mgr.one_call(town.lat, town.lon)
        forecast = one_call.forecast_daily
        temp = w.temperature('celsius')['temp']
        answer = "В городе "+message.text+" сейчас "+w.detailed_status+"\n"
        answer += "Температура в районе "+str(temp)+"\n\n"
        answer += "Завтра в это же время ожидается "+forecast[0].detailed_status+"\n"
        answer += "Температура утром "+str(forecast[0].temperature('celsius')['morn']) \
                  +", днем "+str(forecast[0].temperature('celsius')['day']) \
                  +", вечером "+str(forecast[0].temperature('celsius')['eve']) \
                  +", ночью "+str(forecast[0].temperature('celsius')['night'])

        bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
