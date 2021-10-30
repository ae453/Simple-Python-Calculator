# add functionality to find the the area of a circle using the pi constant

import time
from features import *


def start():
    print("What calculator functionality should the program execute?")
    print("Absolute Value (abs)...\nRegular Calculator (reg)...\nGreatest Common Divisor (gcd)\n")
    do = input("Input Here: ")
    if do == "abs":
        absolute_value()
    elif do == "reg":
        reg()
    elif do == "gcd":
        greatest_common_divisor()
    elif do == "continue":
        pass
    else:
        exit_input = input("You typed in an non-existing functionality.\nWould you like to exit the program?: ")
        if exit_input == "y":
            exit()
        elif exit_input == "n":
            print("\n"*5)
            pass
        else:
            print("You typed in an incorrect answer.\nTry again later.")
            exit()


while True:
    print("\nPlease Wait\nDON'T PRESS ANYTHING")
    time.sleep(2.5)
    print("\n"*80)
    start()
    if True:
        continue2 = input("\nWould you like to continue? (y or n): ")
        if continue2 == "y":
            pass
        elif continue2 == "n":
            print("\nOkay Bye")
            quit()
        else:
            print("Well, you answered wrong.\nTry again later.")
            quit()