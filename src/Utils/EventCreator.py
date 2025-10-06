import json
from dataclasses import asdict
from typing import List

from Classes import Event, Choice, EventTime
e: Event
description: str
eventTime = int
choices: List[Choice]
c: Choice
name: str
choicedesc: str
duration: int
hpChange: int
attackChange: int
defenseChange: int
charismaChange: int
events: List[Event] = []

with open ("db.json", "r") as file:
    raw = json.load(file)
events = [
    Event(
        s["code"],
        s["description"],
        s["eventTime"],
        [Choice(**c)for c in s["choices"]]
    )
    for s in raw
]

print("Welcome to the Event Creation page!")

#Event's description input
check = True
while check:
    description = input("Write the event description: ")
    if description == "" or description == None:
        print("Please, input a description")
    else:
        check = False

#Event's range of action input
check = True
while check:
    print("MORNING = 1, AFTERNOON = 2, EVENING = 3")
    try:
        eventTime = int(input("Input the event's range of action: "))
        if eventTime != 1 and eventTime != 2 and eventTime != 3:
            print("Invalid input")
        else:
            check = False
    except ValueError:
        print("Invalid input")

e = Event(len(events)+1,description,EventTime(eventTime),[])

print("Time to describe the first choice!")
counter = 1
choiceBool = True
while choiceBool:
    check = True
    while check:
        name = input(f"Input the N°{counter} choice name: ")
        if name == "" or name == None:
            print("Please, input a name")
        else:
            check = False

    check = True
    while check:
        try:
            duration = int(input("Input how long the choice would take in minutes: "))
            if duration <0:
                print("Invalid input")
            else:
                check = False
        except ValueError:
            print("Invalid input")

    check = True
    while check:
        choicedesc = input(f"Input the N°{counter} choice description: ")
        if choicedesc == "" or choicedesc == None:
            print("Please, input a description")
        else:
            check = False

    check = True
    while check:
        try:
            print("Input how the choice's would affect the player's HP")
            print("Input a >0 value for healing, <0 for damage, 0 for no affection")
            hpChange = int(input("Amount: "))
            check = False
        except ValueError:
            print("Invalid input")

    check = True
    while check:
        try:
            print("Input how the choice's would affect the player's ATTACK")
            print("Input a >0 value to increase, <0 to decrease, 0 for no affection")
            attackChange = int(input("Amount: "))
            check = False
        except ValueError:
            print("Invalid input")

    check = True
    while check:
        try:
            print("Input how the choice's would affect the player's DEFENSE")
            print("Input a >0 value to increase, <0 to decrease, 0 for no affection")
            defenseChange = int(input("Amount: "))
            check = False
        except ValueError:
            print("Invalid input")

    check = True
    while check:
        try:
            print("Input how the choice's would affect the player's CHARISMA")
            print("Input a >0 value to increase, <0 to decrease, 0 for no affection")
            charismaChange = int(input("Amount: "))
            check = False
        except ValueError:
            print("Invalid input")

    c = Choice(name, counter, choicedesc, duration,
               hpChange, attackChange, defenseChange, charismaChange)
    e.choices.append(c)

    if counter == 1:
        counter += 1
    else:
        if counter < 4:
            option = input("Want to add another choice [Y/N]?")
            checkInput = True
            while checkInput:
                if option.lower() == "y":
                    counter+=1
                    checkInput = False
                else:
                    if option.lower() == "n":
                        choiceBool = False
                        checkInput = False
                    else:
                        print("Invalid Input")
        else:
            choiceBool = False

events.append(e)
event_dicts = [asdict(k) for k in events]
with open ("db.json", "w") as file:
    json.dump(event_dicts,file,indent=4)