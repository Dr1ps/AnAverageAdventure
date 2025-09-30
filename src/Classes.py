from contextlib import nullcontext
from datetime import datetime, time, timedelta

from pip._internal.utils.misc import enum


class Player:
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

    def to_dict(self):
        return {"name": self.name, "hp": self.hp}

class Day:
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

class EventTime(enumerate):
    MORNING = 1
    AFTERNOON = 2
    EVENING = 3

class Event:
    def __init__ (self,code,description,eventTime,choices,duration):
        self.code = code
        self.description = description
        if eventTime == 1:
            self.eventTime = EventTime.MORNING
        else:
            if eventTime == 2:
                self.eventTime = EventTime.AFTERNOON
            else:
                if eventTime == 3:
                    self.eventTime = EventTime.EVENING
        self.choices = choices
        self.duration = duration
    def getChoiceById (self,code):
        for i in self.choices:
            if i.code == code:
                return i
        return nullcontext

class Choice:
    def __init__(self,name,code,description):
        self.name = name
        self.code = code
        self.description = description



