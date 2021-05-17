# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import colorama
from colorama import Fore, Back, Style

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print("I \"love\" onion") # Экранирование
    print("Hello \nworld") # перенос строки
    myname = "Owlya"
    age = 23
    print("Hi, my name is " + myname + "!")
    print("I am " + str(age) + " years old") # Convert to string
    username = input("Input your name: ")
    userage = input("Input your age: ")
    print("Hi, I am " + username + ", i am " + userage + " years old") # Все, что вводит пользователь - строка!
    calculator()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
