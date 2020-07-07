import pynput
from pynput.keyboard import Key, Controller
import time
import random

option = ""
delay = 0
keyboard = Controller()
break_loop = False
first_time = True

while True:
    if first_time:
        print("""loaded typer.py - paste in your text, type the delay press enter and select the text area with your cursor\n(made with tyings.gg in mind so it probably works the best for that site)""")
        first_time = False

    if break_loop:
        print("\nclosed typer.py")
        break

    print("\nenter the text you wish to type")
    text = input("> ")

    text = text.split(" ")

    print("\nenter the delay range after every key (0.100 = 100 ms !make sure the number is three digits!)")
    print("example: 0.150-0.075 ms = 100±5 wpm")
    delay_after_from = float(input("from: "))
    delay_after_to = float(input("to: "))

    print("\ntyping will start shortly..")

    time.sleep(0.7)
    print("\n3..")
    time.sleep(0.7)
    print("2..")
    time.sleep(0.7)
    print("1..")

    for word in text:
        for char in word:
            delay_after = random.uniform(
                delay_after_from, delay_after_to)

            keyboard.press(char)
            keyboard.release(char)
            time.sleep(delay_after)

        delay_after = random.uniform(
            delay_after_from, delay_after_to)

        keyboard.press(Key.space)
        keyboard.release(Key.space)
        time.sleep(delay_after)

    print("\nfinished typing\n")

    print("do you want to continue? (y/n)")

    while True:
        option = input("> ")

        if option.lower().strip() == "n":
            break_loop = True
            break
        elif option.lower().strip() == "y":
            break
        else:
            print("invalid input")
