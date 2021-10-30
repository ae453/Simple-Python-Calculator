import math


def absolute_value():
    try:
        print("Absolute Value Selected.\nUse '*','/','+',and '-'\n")
        abs_expression = eval(input("Expression: "))
    except Exception as e:
        print("\n", e, "\nTry again later.")
    else:
        print(math.fabs(abs_expression))
    finally:
        print("\nOperation Complete")


def reg():
    try:
        print("Regular Calculator Selected.\nUse '*','/','+',and '-'\n")
        reg_expression = eval(input("Expression: "))
    except Exception as e:
        print("\n", e, "\nTry again later.")
    else:
        print(reg_expression)
    finally:
        print("\nOperation Complete")


def greatest_common_divisor():
    try:
        print("Greatest Common Divisor Selected.\nPick Two Integers, No Floating Points\n")
        gcd_num1 = int(input("First Number\nInput Here: "))
        gcd_num2 = int(input("\nSecond Number\nInput Here: "))
    except Exception as e:
        print("\n", e, "\nTry again later.")
    else:
        print(math.gcd(gcd_num1, gcd_num2))
    finally:
        print("\nOperation Complete")