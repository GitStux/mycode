#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'west': 'Treasure Room',
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key'
    },

    'Kitchen': {
        'north': 'Hall',
        'item': 'monster',
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'red potion'
    },
    'Garden': {
        'north': 'Dining Room',
        'down': 'Treasure Room'
    },
    'Treasure Room': {
        'east': 'Hall',
        'item': 'glowing chest of lootz',
        'boss': 'Molag bal',
        'up': 'Garden'
    }
}

potions = {
    "orange": "invisibility",
    "blue": "strength",
    "green": "speed",
    "red": "health"
}

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# loop forever
while True:

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    # ~~~MOVEMENT THROUGH ROOMS~~~#
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    # ONLY SPLITS 1 TIME. THE REST IS 1 SOLID STRING
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            showStatus()
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item'] and "boss" not in rooms[currentRoom]:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
            showStatus()
        # otherwise, if the item isn't there to get
        elif rooms[currentRoom]["boss"]:
            print(f"{rooms[currentRoom]['boss']} drops down!!\nBattle! ")
            while "boss" in rooms[currentRoom]:
                print("**************************************************")
                player_attack = input(
                    "Battle Molag bal for the sweet lootz, Press (1) for punch or (2) for roundhouse kick! ")
                if player_attack == "2":
                    print("**********************************************")
                    print("Molag bal's only weakness is the roundhouse kick, nicely done. \n" + move[1] + " got!")
                    print("--------------------------------------")
                    print("Molag bal trophy added to inventory. ")
                    print("--------------------------------------")
                    print("A small light shines from above.....")
                    inventory.append(move[1])
                    inventory.append("~~Head of Molag bal~~")
                    del rooms[currentRoom]["boss"]
                    del rooms[currentRoom]["item"]

                    showStatus()
                else:
                    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                    print("Molag bal laughs at your puny punch! \n GAME OVER!")
                    exit(0)

    if move[0] == "use":
        if "red potion" in inventory:
            print(f"The red potion is for {potions['red'].upper()}. \nFeeling refreshed.")


        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
            showStatus()

    # ~~~~~ GAME WINNING SITUATIONS ~~~~~~#
    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

        ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
    elif currentRoom == 'Garden' and "~~Head of Molag bal~~" in inventory:
        print('You found the secret passage after defeating Molag bal. VICTORY!')
        break

