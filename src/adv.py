import random
from room import Room
from item import Item
from player import Player
from colored import fg, bg, attr
import os
from lightsource import LightSource


def clear(): return os.system('cls' if os.name == 'nt' else 'clear')


# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
    "corona": Room("Streets", "Corona virus infested streets 👑🦠🛣️,\nPlease use a mask 😷", True),
    "city": Room("City", "Corona virus infested city 👑🦠🏙️, \nPlease use a mask 😷", True),
}


# # Link rooms together

room["outside"].n_to = room["foyer"]
room["outside"].s_to = room["corona"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]
room["corona"].s_to = room["city"]


room["outside"].items.append(Item("sword", "Long Sword"))
room["outside"].items.append(Item("coins", "Gold Coins"))


# Gets random room and puts the torch there
key, random_room = random.choice(list(room.items()))
random_room.items.append(LightSource("torch", "Torch"))


#
# Main
#

# Make a new player object that is currently in the 'outside' room.


player = Player("Rodrigo", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


print("Lets play a game?")


def menu():
    print()
    print(player)
    print("Where do you wanna go next? 🤔")
    print("Choose one:")
    print("\tn: Move north 👆")
    print("\ts: Move south 👇")
    print("\tw: Move west 👈")
    print("\te: Move down 👉")
    print("\ti: See inventory 👜")
    print("\tl: Look around 👀")
    print(" get Item: Pick up stuff ⛏️")
    print("drop Item: Drop stuff 💧")
    print("\tq: Exit 🚪🚶")
    print()


option = None

while option != "q":
    menu()

    option = str(input("Whats gonna be? "))
    print()

    clear()

    if option in ["n", "s", "w", "e"]:
        player.move(option)
    if option == "l":
        if not player.current_room.is_light:
            print("It's pitch black!")
        if len(player.current_room.items):
            print("%sYou see: %s%s" %
                  (fg(2), player.current_room.items, attr(0)))
        else:
            print("%sYou see nothing 👁️%s" %
                  (fg(2), attr(0)))
    if option == "i" or option == "inventory":
        print("%sYour inventory: %s%s" % (fg(11), player.inventory, attr(0)))

    if option.count(" "):
        options = option.split()
        if options[0] == "get" or options[0] == "take":
            player.pickItem(options[1])
        if options[0] == "drop":
            player.dropItem(options[1])


print("The end\n")
