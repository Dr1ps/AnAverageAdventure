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
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp

    def getName(self):
        return self.name

    def damage(self,amount):
        self.hp = self.hp - amount
        print(f"Ouch! Damage taken! -{amount}")

    def heal(self,amount):
        self.hp = self.hp + amount
        print(f"Healed self by +{amount}")

@dataclass
class Day:
    dayNumber: int
    hour: time
    def __init__(self):
        self.dayNumber = 0
        self.hour = time(8,0)

    def addTime(self,time):
        seconds = timedelta(hours=self.hour.hour, minutes=self.hour.minute)
        seconds = seconds + time
        newHour = seconds // 3600
        newMinute = seconds // 60
        if newMinute > 59:
            newMinute = newMinute - 60
            newHour = newHour + 1
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
    def __init__(self,name,code,description,duration):
        self.name = name
        self.code = code
        self.description = description
        self.duration = duration

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
        return nullcontext



