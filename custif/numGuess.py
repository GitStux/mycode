#!/usr/bin/env python3

import random

rand = random.randint(1, 20)

askMoar = True 
round = 0

while askMoar:
    round += 1
    
    try:
        guess = int(input("Guess a number between 1 - 20: ").strip())
        if guess == rand:
            print("congrats the number is " + str(rand))
            askMoar = False
            break

        elif round == 3:
            print("the number is close to "+ str((rand - 2)))

        elif round == 5:
            print("sorry you lose the number was " + str(rand))
            askMoar = False
            break

        else:
            print("So close, but definitely wrong.")
    except:
        print("Numbers are located at the top of your keyboard")

football = input("Greatest football team of all time? ").strip().lower()

if football != "raiders":
    print("FALSE!!")
    print(football + " doesn't look like the Raiders!")

else:
    print("You're a real one")



while True:

    superbowl = input("What teams have never won a Super Bowl? ").strip().lower()

    superBowlLosers = {
            "0": "browns",
            "1": "titans",
            "2": "chargers",
            "3": "bengals",
            "4": "bills",
            "5": "cardinals",
            "6": "falcons",
            "7": "jaguars",
            "8": "lions",
            "9": "panthers",
            "10": "texans",
            "11": "vikings"
            }
    
    if superbowl in superBowlLosers.values():
        print(f"Yes the {superbowl} are painfully average. ")
        break
