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
class concolours:
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

class item:
    def __init__(self, name, description, getable, classrestr, rarity, dmgmod, defmod, useaction=None):
        self.name = name,
        self.description = description,
        self.getable = getable,
        self.classrestr = classrestr,
        self.rarity = rarity,
        self.dmgmod = dmgmod,
        self.defmod = defmod,
        self.useaction = useaction

#init objects from objectdata file.
items = {item.name : item for item in yaml.load_all(objectdata)}

#init rooms from roomdata file:
rooms = {}
for data in yaml.load_all(roomdata):
    rooms.update(data)


# stores the players in the game
players = {}

# start the server
mud = MudServer()

## initialisations
def init_player():
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
            "inventory": [],
            "access": [],
            "room": "Medical Bay",
        }

        # send the new player a prompt for their name
        mud.send_message(id,"                   TRITON\n", concolours.DARKRED)
        mud.send_message(id,"\"Corruption is thrown around a lot these days. The corrupted engines, the corruption of our computer system, the corruptive growths. People who say it, don't understand what it means. What we have here isn't corruption...It's evolution.\" - Roger Valiun \n \n", concolours.DARKRED)
        mud.send_message(id, "~INTERUPT~ \n TELL ME WANDERER, What is your NAME?", concolours.BOLD)

def init_class():
    cl = command
    if cl in ['medic', 'marine', 'engineer']:
        players[id]["class"] = cl
        mud.send_message(id, "WELL WANDERER. It seems YOU ARE A %s. I will SET YOU FREE on this ship. Enjoy your time." % players[id]["class"], concolours.BOLD)
                # send the new player the description of their current room
        if cl == 'medic':
            players[id]["inventory"] = ['bandage','bandage']
            players[id]["access"].append("medic")
        if cl == 'marine':
            players[id]["inventory"] = ['pipe']
            players[id]["hp"] += 25
            players[id]["access"].append("marine")
        if cl == 'engineer':
            players[id]["inventory"] = ['pipe', 'pipe']
            players[id]["hp"] -= 10
            players[id]["access"].append("engineer")
        mud.send_message(id, rooms[players[id]["room"]]["description"], concolours.NORMAL)
    else:
        mud.send_message(id, "That is not a VALID OCCUPATION. I TOLD YOU THE OPTIONS wanderer.", concolours.BOLD)

def init_room():
    # go through all the players in the game and tell them a player has entered.
    rm = rooms[players[id]["room"]]
    for pid,pl in players.items():
        # if player is in the same (new) room and isn't the player sending the command
        if players[pid]["room"] == players[id]["room"] and pid!=id:
            # send them a message telling them that the player entered the room
             mud.send_message(pid,players[id]["name"] + " has arrived.")

    # send the player a description of the room.
    mud.send_message(id, rm["description"], concolours.OKBLUE)


## player commands

def pcommlook():
            # store the player's current room
            rm = rooms[players[id]["room"]]

            # send the player back the description of their current room
            mud.send_message(id, rm["description"], concolours.NORMAL)

            if rm["corruption"] >= 20 and rm["corruption"] < 50:
                mud.send_message(id,"There are small signs of corruption seeping in.", concolours.DARKRED)
            elif rm["corruption"] > 50:
                mud.send_message(id,"Corruption is taking hold of the area.", concolours.DARKRED)

            playershere = []
            # go through every player in the game
            for pid,pl in players.items():
                # if they're in the same room as the player
                if players[pid]["room"] == players[id]["room"]:
                    # add their name to the list
                    playershere.append(players[pid]["name"])

            # send player a message containing the list of players in the room
            mud.send_message(id, "Players here: %s" % ", ".join(playershere), concolours.LIGHTGREEN)

            # send player a message containing the list of exits from this room
            if rm["north"] is not None:
                mud.send_message(id, "To the North is: " + rm["north"], concolours.OKBLUE)
            if rm["east"] is not None:
                mud.send_message(id, "To the East is: " + rm["east"], concolours.OKBLUE)
            if rm["south"] is not None:
                mud.send_message(id, "To the South is: " + rm["south"], concolours.OKBLUE)
            if rm["west"] is not None:
                mud.send_message(id, "To the South is: " + rm["west"], concolours.OKBLUE)

            if len(rm["objects"]) != 0:
                mud.send_message(id,"You see here: " + str(rm["objects"]), concolours.LIGHTGREEN)

def pcommsay():

            # go through every player in the game
            for pid,pl in players.items():
                # if they're in the same room as the player
                if players[pid]["room"] == players[id]["room"]:
                    # send them a message telling them what the player said
                    mud.send_message(pid,"%s says: %s" % (players[id]["name"],params) )

def pcommemote():
        # go through every player in the game
        em = params.lower()
        for pid,pl in players.items():
            # if they're in the same room as the player
            if players[pid]["room"] == players[id]["room"]:
                # send them a message telling them what the player said
                mud.send_message(pid, players[id]["name"] + params, concolours.EMOTE)

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

def pcommchar():
    mud.send_message(id, "Name:" + players[id]["name"])
    mud.send_message(id, "Designation:" + players[id]["class"])
    mud.send_message(id, "Health:" + players[id]["hp"])

def pcommdirection():
            # store the exit name
        direction = params.lower()

        # store the player's current room
        rm = rooms[players[id]["room"]]
        prevrm = rooms[players[id]["room"]]

        # go through all the players in the game
        for pid,pl in players.items():
            # if player is in the same room and isn't the player sending the command
            if players[pid]["room"] == players[id]["room"] and pid!=id:
                # send them a message telling them that the player left the room
                mud.send_message(pid,"%s left to the '%s'" % (players[id]["name"],command))

            # update the player's current room to the one the exit leads to
        if (command == "north" or command == "n") and rm["north"] is not None:
                prevrm = players[id]["room"]
                players[id]["room"] = rm["north"]
                if rmrestrictioncheck(rm["restriction"]) == True:
                    mud.send_message(id,"You arrive at '%s'" % players[id]["room"])
                else:
                    players[id]["room"] = prevrm

        elif (command == "east" or command == "e") and rm["east"] is not None:
                prevrm = players[id]["room"]
                players[id]["room"] = rm["east"]
                if rmrestrictioncheck(rm["restriction"]) == True:
                    mud.send_message(id,"You arrive at '%s'" % players[id]["room"])
                else:
                    players[id]["room"] = prevrm

        elif (command == "south" or command == "s") and rm["south"] is not None:
                prevrm = players[id]["room"]
                players[id]["room"] = rm["south"]
                if rmrestrictioncheck(rm["restriction"]) == True:
                    mud.send_message(id,"You arrive at '%s'" % players[id]["room"])
                else:
                    players[id]["room"] = prevrm

        elif (command == "west" or command == "w") and rm["west"] is not None:
                prevrm = players[id]["room"]
                players[id]["room"] = rm["west"]
                if rmrestrictioncheck(rm["restriction"]) == True:
                    mud.send_message(id,"You arrive at '%s'" % players[id]["room"])
                else:
                    players[id]["room"] = prevrm

        elif (command == "up" or command == "u") and rm["up"] is not None:
                prevrm = players[id]["room"]
                players[id]["room"] = rm["up"]
                if rmrestrictioncheck(rm["restriction"]) == True:
                    mud.send_message(id,"You arrive at '%s'" % players[id]["room"])
                else:
                    players[id]["room"] = prevrm

        elif (command == "down" or command == "d") and rm["down"] is not None:
                prevrm = players[id]["room"]
                players[id]["room"] = rm["down"]
                if rmrestrictioncheck(rm["restriction"]) == True:
                    mud.send_message(id,"You arrive at '%s'" % players[id]["room"])
                else:
                    players[id]["room"] = prevrm


        else:
            # send back an 'unknown exit' message
            mud.send_message(id, "You cannot go in that direction")

        #init the room (tell players stuff, set variables)
        init_room()

def rmrestrictioncheck(roomrest):
    #print r
    print roomrest
    print players[id]["access"]
    if roomrest in players[id]["access"] or roomrest == "":
        return True
    else:
        mud.send_message(id,"You do not have the correct credentials to enter '%s'" % players[id]["room"])
        return False

#item manipluation
def pcommget():
    it = params.lower()
    rm = rooms[players[id]["room"]]
    #check if it's in both the items list and the object list of the room
    if it in items and it in rm["objects"]:
        chosenitem = items[it]
        if chosenitem.getable:
            players[id]["inventory"].append(it)
            rm["objects"].remove(it)
            mud.send_message(id, "You pick up a " + it)
        else:
            mud.send_message(id, "You can't pick that up")
    else:
        mud.send_message(id, "That object isn't here.")

def pcommdrop():
    it = params.lower()
    rm = rooms[players[id]["room"]]
    #check if it's in the item list and the inventory list
    if it in items and it in players[id]["inventory"]:
        players[id]["inventory"].remove(it)
        rm["objects"].append(it)
        mud.send_message(id, "You drop a " + it)
    else:
        mud.send_message(id, "You don't have that object")

def pcommuse():
    it = params.lower()
    rm = rooms[players[id]["room"]]
    #check if it's in both the items list and the object list of the room
    if it in items and (it in rm["objects"] or it in players[id]["inventory"]):
        chosenitem = items[it]
        chosenitem.useaction()

def pcommexamine():
    it = params.lower()
    rm = rooms[players[id]["room"]]
    #check if it's in both the items list and the object list of the room
    if it in items and (it in rm["objects"] or it in players[id]["inventory"]):
        chosenitem = items[it]
        mud.send_message(id, chosenitem.description)
    else:
        mud.send_message(id, "That is not here.")

def pcomminventory():
    if len(players[id]["inventory"]) != 0:
        mud.send_message(id, "You have:" + str(players[id]["inventory"]))
    else:
        mud.send_message(id, "You don't have anything")


#sys commands
def pcommhelp():
                # send the player back the list of possible commands
            mud.send_message(id,"Commands:")
            mud.send_message(id,"  say <message>  - Says something out loud, e.g. 'say Hello'")
            mud.send_message(id,"  emote <message>- conveys an actions '*bows deeply*'")
            mud.send_message(id,"  inv/inventory  - examines your inventory")
            mud.send_message(id,"  get/take       - takes an item and puts it in your inventory")
            mud.send_message(id,"  drop           - drops an item on the ground")
            mud.send_message(id,"  char           - examines yourself")
            mud.send_message(id,"  look           - Examines the surroundings, e.g. 'look'")
            mud.send_message(id,"  go <exit>      - Moves through the exit specified, e.g. 'go outside'")
            mud.send_message(id,"  quit           - Quits the game")

def pcommquit():
    mud.send_message(id,"You have left the Antikylton.", concolours.BOLD)
    mud._handle_disconnect(id)

def itemheal():
    players[id]["hp"] = 100
    mud.send_message(id,"You are healed")

def itembash():
    mud.send_message(id,"you bash everything!")
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

    init_player()

    # go through any recently disconnected players
    for id in mud.get_disconnected_players():

        # if for any reason the player isn't in the player map, skip them and
        # move on to the next one
        if id not in players: continue

        # go through all the players in the game
        for pid, pl in players.items():
            # send each player a message to tell them about the diconnected player
            mud.send_message(pid,"%s quit the game" % players[id]["name"], concolours.BOLD)

        # remove the player's entry in the player dictionary
        del(players[id])


    # go through any new commands sent from players
    for id,command,params in mud.get_commands():

        # if for any reason the player isn't in the player map, skip them and
        # move on to the next one
        if id not in players: continue

    #FIRST TIME BLOCK
        # if the player hasn't given their name yet, use this first command as their name
        if players[id]["name"] is None:

            players[id]["name"] = command
            # tell all players a new player has arrived.

            for pid,pl in players.items():
                # send each player a message to tell them about the new player
                mud.send_message(pid,"%s entered the game" % players[id]["name"], concolours.BOLD)

            mud.send_message(id,"~BANK4CORRUPTIONPROTOCOL~\n WELCOME, %s. CHOOSE YOUR designation, PLEASE: 'Engineer', 'Marine' or 'Medic'." % players[id]["name"], concolours.BOLD)
        elif players[id]["name"] is not None and players[id]["class"] is None:
            #init class stuff (starting items etc.)
            init_class()


    # each of the possible commands is handled below.

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

        #directions
        elif command in ("north", "n", "east", "e", "south", "s", "west", "w", "up", "u", "down", "d"):
            pcommdirection()

        #inventory
        elif command in ("inventory", "i", "inv"):
            pcomminventory()

        #character
        elif command in ("char", "character"):
            pcommchar()

        #use command
        elif command in ("use", "u"):
            pcommuse()

        # 'go' command
        elif command == "go":
            pcommgo()

        #item commands

        elif command in ("get", "take"):
            pcommget()

        elif command in ("drop", "throw"):
            pcommdrop()

        elif command in ("examine", "describe"):
            pcommexamine()

        #sys commands
        elif command == "quit":
            pcommquit()

        # some other, unrecognised command
        else:
            # send back an 'unknown command' message
            mud.send_message(id, "Unknown command '%s'" % command, concolours.WARNING)

