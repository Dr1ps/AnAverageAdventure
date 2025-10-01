from email.headerregistry import DateHeader

from Classes import Player, Event, Day, Choice, EventTime
from Manager import Manager

player = Player("Micheal",100)

day = Day()

manager = Manager (player, day)

print("A new adventurer! Let's begin!")
print(f"Micheal({player.hp}hp)")

manager.trigger()

