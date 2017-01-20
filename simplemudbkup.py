"""    
A simple Multi-User Dungeon (MUD) game. Players can talk to each other, examine
their surroundings and move between rooms.

Some ideas for things to try adding:
    * More rooms to explore
    * An 'emote' command e.g. 'emote laughs out loud' -> 'Mark laughs out loud'
    * A 'whisper' command for talking to individual players
    * A 'shout' command for yelling to players in all rooms
    * Items to look at in rooms e.g. 'look fireplace' -> 'You see a roaring, glowing fire'
    * Items to pick up e.g. 'take rock' -> 'You pick up the rock'
    * Monsters to fight
    * Loot to collect
    * Saving players accounts between sessions
    * A password login
    * A shop from which to buy items

author: Mark Frimston - mfrimston@gmail.com
"""

import time
import yaml


# import the MUD server class
from mudserver import MudServer
from roomdata import roomdata
from objectdata import objectdata

#class for console colours
class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    DARKRED = '\033[1;31;40m'
    LIGHTGREEN = '\033[1;32;40m'
    WARNING = '\033[93m'
    EMOTE = '\033[1;221;40m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = "\033[1m"
    UNDERLINE = '\033[4m'
    NORMAL = '\033[0;37;40m'

# structure defining the rooms in the game. Try adding more rooms to the game!

#init objects from objectdata file
objects = {}
for data in yaml.load_all(objectdata):
    objects.update(data)

#init rooms from roomdata file
rooms = {}
for data in yaml.load_all(roomdata):
    rooms.update(data)


# stores the players in the game
players = {}

# start the server
mud = MudServer()

def pcommhelp():
                # send the player back the list of possible commands
            mud.send_message(id,"Commands:")
            mud.send_message(id,"  say <message>  - Says something out loud, e.g. 'say Hello'")
            mud.send_message(id,"  look           - Examines the surroundings, e.g. 'look'")
            mud.send_message(id,"  go <exit>      - Moves through the exit specified, e.g. 'go outside'")
            mud.send_message(id,"  quit           - Quits the game")

def pcommlook():
            # store the player's current room
            rm = rooms[players[id]["room"]]

            # send the player back the description of their current room
            mud.send_message(id, rm["description"], bcolors.NORMAL)

            if rm["corruption"] >= 20 and rm["corruption"] < 50:
                mud.send_message(id,"There are small signs of corruption seeping in.", bcolors.DARKRED)
            elif rm["corruption"] > 50:
                mud.send_message(id,"Corruption is taking hold of the area.", bcolors.DARKRED)

            playershere = []
            # go through every player in the game
            for pid,pl in players.items():
                # if they're in the same room as the player
                if players[pid]["room"] == players[id]["room"]:
                    # add their name to the list
                    playershere.append(players[pid]["name"])

            # send player a message containing the list of players in the room
            mud.send_message(id, "Players here: %s" % ", ".join(playershere), bcolors.LIGHTGREEN)

            # send player a message containing the list of exits from this room
            if rm["north"] is not None:
                mud.send_message(id, "To the North is: " + rm["north"], bcolors.OKBLUE)
            if rm["east"] is not None:
                mud.send_message(id, "To the East is: " + rm["east"], bcolors.OKBLUE)
            if rm["south"] is not None:
                mud.send_message(id, "To the South is: " + rm["south"], bcolors.OKBLUE)
            if rm["west"] is not None:
                mud.send_message(id, "To the South is: " + rm["west"], bcolors.OKBLUE)

def pcommsay():

            # go through every player in the game
            for pid,pl in players.items():
                # if they're in the same room as the player
                if players[pid]["room"] == players[id]["room"]:
                    # send them a message telling them what the player said
                    mud.send_message(pid,"%s says: %s" % (players[id]["name"],params) )

def pcommgo():
            # store the exit name
        ex = params.lower()

        # store the player's current room
        rm = rooms[players[id]["room"]]

        # if the specified exit is found in the room's exits list
        if ex in rm["exits"]:

            # go through all the players in the game
            for pid,pl in players.items():
                # if player is in the same room and isn't the player sending the command
                if players[pid]["room"] == players[id]["room"] and pid!=id:
                    # send them a message telling them that the player left the room
                    mud.send_message(pid,"%s left via exit '%s'" % (players[id]["name"],ex))

            # update the player's current room to the one the exit leads to
            players[id]["room"] = rm["exits"][ex]
            rm = rooms[players[id]["room"]]

            # go through all the players in the game
            for pid,pl in players.items():
                # if player is in the same (new) room and isn't the player sending the command
                if players[pid]["room"] == players[id]["room"] and pid!=id:
                    # send them a message telling them that the player entered the room
                    mud.send_message(pid,"%s arrived via exit '%s'" % (players[id]["name"],ex))

            # send the player a message telling them where they are now
            mud.send_message(id,"You arrive at '%s'" % players[id]["room"])

        # the specified exit wasn't found in the current room
        else:
            # send back an 'unknown exit' message
            mud.send_message(id, "Unknown exit '%s'" % ex)

def pcommdirection():
            # store the exit name
        direction = params.lower()

        # store the player's current room
        rm = rooms[players[id]["room"]]

        # go through all the players in the game
        for pid,pl in players.items():
            # if player is in the same room and isn't the player sending the command
            if players[pid]["room"] == players[id]["room"] and pid!=id:
                # send them a message telling them that the player left the room
                mud.send_message(pid,"%s left to the '%s'" % (players[id]["name"],command))

            # update the player's current room to the one the exit leads to
        if (command == "north" or command == "n") and rm["north"] is not None:
            players[id]["room"] = rm["north"]
            # send the player a message telling them where they are now
            mud.send_message(id,"You arrive at '%s'" % players[id]["room"])

        elif (command == "east" or command == "e") and rm["east"] is not None:
            players[id]["room"] = rm["east"]
            # send the player a message telling them where they are now
            mud.send_message(id,"You arrive at '%s'" % players[id]["room"])

        elif (command == "south" or command == "s") and rm["south"] is not None:
            players[id]["room"] = rm["south"]
            # send the player a message telling them where they are now
            mud.send_message(id,"You arrive at '%s'" % players[id]["room"])

        elif (command == "west" or command == "w") and rm["west"] is not None:
            players[id]["room"] = rm["west"]
            # send the player a message telling them where they are now
            mud.send_message(id,"You arrive at '%s'" % players[id]["room"])

        else:
            # send back an 'unknown exit' message
            mud.send_message(id, "You cannot go in that direction")

            # go through all the players in the game
        for pid,pl in players.items():
            # if player is in the same (new) room and isn't the player sending the command
            if players[pid]["room"] == players[id]["room"] and pid!=id:
                # send them a message telling them that the player entered the room
                mud.send_message(pid,players[id]["name"] + " has arrived.")


#
        # the specified exit wasn't found in the current room

def pcommquit():
    mud.send_message(id,"You have left the Antikylton.", bcolors.BOLD)
    mud._handle_disconnect(id)

def pcommsetclass():
    cl = params.lower()

    if players[id]["class"] is None:

        mud.send_message(id,"Choose a class: Engineer, Marine, Medic")

        if cl in ['medic', 'marine', 'engineer']:
            players[id]["class"] = cl
            mud.send_message(id, "You are a %s" %players[id]["class"], bcolors.BOLD)

        else:
            mud.send_message(id, "That is not a valid class", bcolors.WARNING)

    else:
        mud.send_message(id,"you have already set a class")

def pcommemote():
        # go through every player in the game
        em = params.lower()
        for pid,pl in players.items():
            # if they're in the same room as the player
            if players[pid]["room"] == players[id]["room"]:
                # send them a message telling them what the player said
                mud.send_message(pid,players[id]["name"] + params, bcolors.EMOTE)

########################################################################
# Main game loop. We loop forever (i.e. until the program is terminated#
########################################################################
while True:

    # pause for 1/5 of a second on each loop, so that we don't constantly
    # use 100% CPU time
    time.sleep(0.2)

    # 'update' must be called in the loop to keep the game running and give
    # us up-to-date information
    mud.update()


    # go through any newly connected players
    for id in mud.get_new_players():

        # Player and Player stats
        players[id] = {
            "name": None,
            "class": None,
            "hp": 100,
            "str": 10,
            "dex": 10,
            "wis": 10,
            "inventory": {},
            "room": "Medical Bay",
        }

        # send the new player a prompt for their name
        mud.send_message(id, "Welcome aboard the Antiklyton. Tell me, what is your name?", bcolors.NORMAL )


    # go through any recently disconnected players
    for id in mud.get_disconnected_players():

        # if for any reason the player isn't in the player map, skip them and
        # move on to the next one
        if id not in players: continue

        # go through all the players in the game
        for pid, pl in players.items():
            # send each player a message to tell them about the diconnected player
            mud.send_message(pid,"%s quit the game" % players[id]["name"], bcolors.BOLD)

        # remove the player's entry in the player dictionary
        del(players[id])


    # go through any new commands sent from players
    for id,command,params in mud.get_commands():

        # if for any reason the player isn't in the player map, skip them and
        # move on to the next one
        if id not in players: continue

        # if the player hasn't given their name yet, use this first command as their name
        if players[id]["name"] is None:

            players[id]["name"] = command
                    # go through all the players in the game
            for pid,pl in players.items():
                # send each player a message to tell them about the new player
                mud.send_message(pid,"%s entered the game" % players[id]["name"], bcolors.BOLD)

                # send the new player a welcome message
                mud.send_message(id,"Welcome to the Antiklyton, %s. Choose your class by typing 'class' followed by 'Engineer', 'Marine' or 'Medic'. Type 'help' for a list of commands. Have fun!" % players[id]["name"],bcolors.BOLD)

                # send the new player the description of their current room
                mud.send_message(id,rooms[players[id]["room"]]["description"], bcolors.NORMAL)

        # each of the possible commands is handled below. Try adding new commands
        # to the game!

        # 'help' command
        elif command == "help":
            pcommhelp()

        # 'say' command
        elif command == "say":
            pcommsay()

        # 'emote' command
        elif command == "emote":
            pcommemote()

        # 'look' command
        elif command == "look":
            pcommlook()

        elif command in ("north", "n", "east", "e", "south", "s", "west", "w"):
            pcommdirection()

        # 'go' command
        elif command == "go":
            pcommgo()

        elif command == "quit":
            pcommquit()

        elif command == "class":
            pcommsetclass()

        # some other, unrecognised command
        else:
            # send back an 'unknown command' message
            mud.send_message(id, "Unknown command '%s'" % command, bcolors.WARNING)

