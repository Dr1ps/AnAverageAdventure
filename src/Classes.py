import dataclasses
from contextlib import nullcontext
from datetime import datetime, time, timedelta
from enum import Enum
from typing import List
from dataclasses import dataclass

from pip._internal.utils.misc import enum

@dataclass
class Player:
    name: str
    hp: int
    attack: int
    defense: int
    charisma: int
    def __init__(self,name,hp,attack,defense,charisma):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.charisma = charisma

    def hpUpd(self,amount):
        if amount == 0:
            return
        if amount < 0:
            amount = amount + self.defense
            if amount >= 0:
                print("+ You defended yourself, negating all damage!")
            else:
                self.hp = self.hp + amount
                print(f"- Ouch! Damage taken! {amount} HP!")
                if self.hp < 0:
                    self.hp = 0
        else:
            self.hp = self.hp + amount
            print(f"+ Healed self by +{amount}")

    def defenseUpd(self,amount):
        if amount == 0:
            return
        if amount > 0:
            print(f"+ Raised defense by {amount}!")
        else:
            print(f"- Lowered defense by {amount}!")
        self.defense += amount
        if self.defense < 0:
            self.defense = 0

    def attackUpd(self,amount):
        if amount == 0:
            return
        if amount > 0:
            print(f"+ Raised attack power by {amount}!")
        else:
            print(f"- Lowered attack power by {amount}!")
        self.attack += amount
        if self.attack < 0:
            self.attack = 0

    def charismaUpd(self,amount):
        if amount == 0:
            return
        if amount > 0:
            print(f"+ Gained {amount} charisma!")
        else:
            print(f"- Lost {amount} charisma!")
        self.charisma += amount
        if self.charisma < 0:
            self.charisma = 0



@dataclass
class Day:
    dayNumber: int
    hour: time
    def __init__(self):
        self.dayNumber = 1
        self.hour = time(8,0)

    def addTime(self,timeToAdd):
        seconds = (self.hour.hour * 3600) + (self.hour.minute * 60)
        seconds = seconds + (timeToAdd * 60)
        newHour = seconds // 3600
        newMinute = (seconds % 3600) // 60
        if newMinute > 59:
            newMinute = newMinute - (60 * newMinute // 60)
            newHour = newHour + (newMinute // 60)
        if newHour > 23:
            newHour = 8
            newMinute = 0
            self.dayNumber = self.dayNumber + 1
        self.hour = time(newHour,newMinute)

@dataclass
class EventTime(Enum):
    MORNING = 1
    AFTERNOON = 2
    EVENING = 3

@dataclass
class Choice:
    name: str
    code: int
    description: str
    duration: int
    hpChange: int
    attackChange: int
    defenseChange: int
    charismaChange: int
    def __init__(self,name,code,description,duration,hpChange,attackChange,
                 defenseChange,charismaChange):
        self.name = name
        self.code = int(code)
        self.description = description
        self.duration = int(duration)
        self.hpChange = int(hpChange)
        self.attackChange = int(attackChange)
        self.defenseChange = int(defenseChange)
        self.charismaChange = int(charismaChange)

@dataclass
class Event:
    code: int
    description: str
    eventTime: EventTime
    choices: List[Choice]
    def __init__ (self,code,description,eventTime,choices):
        self.code = code
        self.description = description
        self.eventTime = eventTime
        self.choices = choices
    def getChoiceById (self,code):
        for i in self.choices:
            if i.code == code:
                return i
        return None



