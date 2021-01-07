#!/usr/bin/env python3
"""
Author: Matt Janousek

This program calculates user input.
"""

def calculator(num1, num2):
    """Calculator function that takes user input from main() and computes"""
    while True:
        operators = ["+", "-", "/", "*"]
        user_operator = input(f"Please select one of the following operators {operators}: ")


        if user_operator == "+":
            print(num1 + num2)
            break
        elif user_operator == "*":
            print(num1 * num2)
            break
        elif user_operator == "/":
            print(num1 / num2)
            break
        elif user_operator == "-":
            print(num1 - num2)
            break
        else:
            print("you need to select one of the pictured operators!")

def main():
    """Main method that asks for user input, then passes that information to the calculator()"""
    while True:
        try:
            num1 = float(input("Select a number: "))
            num2 = float(input("Select another number: "))
            calculator(num1, num2)
            break
        except:
            print("Please only input numbers. ")

if __name__ == "__main__":
    main()
