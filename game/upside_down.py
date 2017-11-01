#!/usr/bin/python3

import random

class Room():

    def __init__(self, name):
        self.name = name
        self.location = {}
        self.inventory = []
        self.objects = []

    def __str__(self):
        """Describes the room in terms of the name, exits, items, npc's"""
        
	descr = "You are in " + self.name + "\n"
        for key in self.exits:
            descr += "You can go " + key + " to " + self.exits[key].name + "\n"
        for item in self.inventory:
            descr += "There is a " + item.name + " here.\n"
        for item in self.objects:
            descr += item.name + " is here.\n"
	return descr


class Item():

    def __init__(self, name):
        self.name = name

    def name(self, name):
        return self.name

class Player():

    def __init__(self, name, location):
	self.name = name
        self.location = location
        self.inventory = []

    def __str__(self):
        pass

    def get(self, command):
	for item in self.location.inventory:
            if item.name == command[1]:
		self.inventory.append(item)
                self.location.inventory.remove(item)
                print("You picked up a", item.name)
		return
            else:
                print(command[1] + " is not here!")

    def drop(self, command):
        for item in self.inventory:
            if item.name == command[1]:
                self.location.inventory.append(item)
		self.inventory.remove(item)
                print("You dropped a", item.name)
                return
            else:
                print(command[1] + " is not here!")

class NonPlayer(Player):

    def __init__(self, name, location):
        super().__init__(name, location)

class Game():

    def __init__(self):
	pass

    def save(self, name):
        pass

    def load(self, name):
	pass

#directions                                                           
n = 'north'
s = 'south'
e = 'east'
w = 'west'

#instances of each room                                               
one = Room("Room One")
two = Room("Room Two")
three = Room("Room Three")

#Exits 
one.exits[n] = two
one.exits[e] = three
                                                    
two.exits[e] = three
two.exits[s] = one


ame = Game()
p = Player("me", one)
thing = Item("thing")
one.inventory.append(thing)

#NPC                                                                  
#Later on, add random event that will choose which room Fred will appear in, if any at all..                                                
#Fred will be an aggressor, possibly able to move rooms?               
a = NonPlayer("Fred", two)
two.objects.append(a)

command = input("> ").lower().strip().split()

while not command:
    command = input("> ").lower().strip().split()

while command[0] != "quit":
    # Player Commands                                                                                                                           
    if command[0] == "go" and len(command) >= 2:
        if command[1] in p.location.exits.keys():
            p.location = p.location.exits[command[1]]
            print('Okay.')
            print('Successful move')
        else:
            print("I do no understand..")

    elif command[0] == "help":
        print("{}{}{}".format('    ', 'Commands', ' '))
        print("{}{}{}".format('    ', '--------', ' '))
        print("{}{}{}".format('look', '|', 'Explore the room to find current location, exits and potential items.'))
        print("{}{}{}".format('go  ', '|', 'The prefix required to navigate your player.'))
        print("{}{}{}".format('get ', '|', 'The prefix for picking up items.'))
        print("{}{}{}".format('drop', '|', 'The prefix for dropping items.'))
        print("{}{}{}".format('inv ', '|', 'Displays the player inventory'))
        print("{}{}{}".format('save', '|', 'Save current player progress'))
        print("{}{}{}".format('load', '|', 'Load a previous character'))

    elif command[0] == "get" and len(command) >= 2:
        p.get(command)
    elif command[0] == "drop" and len(command) >= 2:
        p.drop(command)
    elif command[0] == "inv":
        #printing the inventory in a box because im cool                                                                                        
        side = '|'
        blank = 30 * " "
        line = 30 *  "-"
        if not p.inventory:
            print("Your inventory is empty.")
        else:
            print("{}{}{}".format('+', line, '+'))
            for item in p.inventory:
                #print("{}{}{}".format(side, blank,  side))                                                                                     
                diff = (30 - len(item.name)) * " "
                print("{}{}{}{}".format(side, item.name, diff, side))
                #print("{}{}{}".format(side, line, side))                                                                                       
                #print("{}{}{}".format(side, blank,  side))                                                                                     
            print("{}{}{}".format('+', line, '+'))

    elif command[0] == 'load':
        game.load(p.name)
    elif command[0] == 'save':
        game.save(p.name)
    elif command[0] == 'look':
        print(p.location)

    command = input("> ").lower().strip().split()
    while not command:
        command = input("> ").lower().strip().split()

    print()
