#!/usr/bin/env python3

user_input= input("What is your name? ")

user_input_day= input("What is the day? ")

print("Hello, ", user_input + "!", "Happy", user_input_day + "!")

# FORMAT
print("Hello {}! Happy {}!".format(user_input, user_input_day))

# F-String

print(f"Hello {user_input}! Happy {user_input_day}!" )
