import json
import random
from ctypes.wintypes import BOOLEAN
from dataclasses import dataclass
from email.headerregistry import DateHeader
from typing import List
from xmlrpc.client import Boolean

from Classes import Event, Player, Day, Choice


@dataclass
class Manager:
    player: Player
    day: Day
    events: List[Event]

    def __init__(self,player,day):
        self.player = player
        self.day = day
        with open ("db.json","r") as file:
            raw = json.load(file)
        self.events = [
            Event(
                s["code"],
                s["description"],
                s["eventTime"],
                [Choice(**c)for c in s["choices"]]
            )
            for s in raw
        ]


    def trigger(self):
        event = self.events[random.randint(1,len(self.events))-1]
        print(event.description)
        for iter in event.choices:
            print(f"{iter.code})"+f"{iter.name}")
        check = True
        chosen: int
        while check:
            try:
                a: str
                a = input("What will you do?: ")
                if a.lower() == "exitpls":
                    return 0
                chosen = int(a)
            except ValueError:
                chosen = 5

            if chosen:
                if event.getChoiceById(chosen):
                    check = False
                else:
                    print("Nonexistent action")
            else:
                print("Error")
                return
        self.triggerChoice(event.getChoiceById(chosen))
        self.status()
        return 1

    def triggerChoice(self,choice):
        print(choice.description)
        self.player.hpUpd(choice.hpChange)
        self.player.attackUpd(choice.attackChange)
        self.player.defenseUpd(choice.defenseChange)
        self.player.charismaUpd(choice.charismaChange)
        self.day.addTime(choice.duration)

    def status(self):
        print("--------------------------------",
            f"{self.player.name} - {self.player.hp} HP\t "
            f"Day:{self.day.dayNumber} - {self.day.hour.strftime("%H:%M")}")











