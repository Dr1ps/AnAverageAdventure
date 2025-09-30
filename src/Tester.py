from email.headerregistry import DateHeader

from Classes import Player, Event, Day, Choice
from Manager import Manager

player = Player("Micheal",100)

choice1 = Choice("Eat it",1,"You ate the can of soup,"
                            "it was expired! Bleah!!!")
choice2 = Choice("Ignore it",2,"You ignored the soup, you thought"
                               "about all the bugs you could find in it.")

choices = {choice1,choice2}

event = Event(1,"You find a can of soup perfectly placed in the center"
                "of a tree stump, it's half eaten and looks appealing.", 1,
              choices,10)
day = Day()
manager = Manager (player, day)

print("A new adventurer! Let's begin!")
print(f"Micheal({player.hp}hp)")
manager.trigger(event)
