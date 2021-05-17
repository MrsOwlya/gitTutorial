# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
from colorama import Fore, Back, Style
import pyowm
import telebot

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def weather():
    owm = pyowm.OWM('1690d76ad190b1a89bf446288d3ad850')
    place = input("Input your location: ")
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather()
    print(w)

def calculator():
    what = input("What to do (+, -, *, /): ")
    a = input("Input first number: ")
    b = input("Input second number: ")
    if what == "+":
        otvet = int(a) + int(b)
        print("Answer is: " + str(otvet))
    elif what == "+":
        otvet = int(a) - int(b)
        print("Answer is: " + str(otvet))
    elif what == "+":
        otvet = int(a) * int(b)
        print("Answer is: " + str(otvet))
    elif what == "+":
        otvet = int(a) / int(b)
        print("Answer is: " + str(otvet))
    else: print("Incorrect symbol!")


bot = telebot.TeleBot("1802555647:AAGV-mNEgc92GxLT2Dlgd2C0PM9MctCGlI8")
@bot.message_handler(content_types=["text"])

def telegrambot(message):
    bot.reply_to(message, message.text)

bot.polling(none_stop=True)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #print("I \"love\" onion") # Экранирование
    #print("Hello \nworld") # перенос строки
    #myname = "Owlya"
    #age = 23
    #print("Hi, my name is " + myname + "!")
    #print("I am " + str(age) + " years old") # Convert to string
    #username = input("Input your name: ")
    #userage = input("Input your age: ")
    #print("Hi, I am " + username + ", i am " + userage + " years old") # Все, что вводит пользователь - строка!
    #calculator()
    #weather()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
