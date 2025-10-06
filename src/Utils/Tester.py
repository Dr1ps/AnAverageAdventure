from email.headerregistry import DateHeader
from operator import truediv

from Classes import Player, Event, Day, Choice, EventTime
from Manager import Manager

print("A new adventurer! Let's begin!")
name = input("What is your name?")

player = Player(name,100,10,0,10)

day = Day()

manager = Manager (player, day)
manager.status()
while True:
    if player.hp == 0:
        print(f"{player.name} died!")
        break
    if day.dayNumber == 10:
        print(f"{player.name} reached their destination, the adventure meets its end")
        break
    if manager.trigger() == 0:
        break

