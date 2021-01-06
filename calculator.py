#!/usr/bin/env python3
"""
Author: Matt Janousek

This program calculates user input.
"""


def calculator():

        try:
            num1 = float(input("Select a number: "))
            num2 = float(input(f"Select another number to do math stuff to {num1}: "))
            operators = ["+", "-", "/", "*"]

            while True:

                user_operator = input(f"Please select one of the following operators {operators}: ")

                if user_operator == "+":
                    print (str(num1 + num2))
                    break
                elif user_operator == "*":
                    print(str(num1 * num2))
                    break

                elif user_operator == "/":
                    print(str(num1 / num2))
                    break

                elif user_operator == "-":
                    print(str(num1 - num2))
                    break


                elif user_operator not in operators:
                    print("you need to select one of the picture operators!")
        except:
            print("need numbers")
            calculator()

if __name__ == "__main__":
    calculator()
