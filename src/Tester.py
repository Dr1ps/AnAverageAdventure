from email.headerregistry import DateHeader

from Classes import Player, Event, Day, Choice, EventTime
from Manager import Manager

print("A new adventurer! Let's begin!")
name = input("What is your name?")

player = Player(name,100)

day = Day()

manager = Manager (player, day)

manager.status()

manager.trigger()

manager.status()