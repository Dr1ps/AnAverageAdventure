from ctypes.wintypes import BOOLEAN
from xmlrpc.client import Boolean


class Manager:
    def __init__(self,player,day):
        self.player = player
        self.day = day

    def trigger(self,event):
        print(event.description)
        for iter in event.choices:
            print(f"{iter.code})"+f"{iter.name}")
        a = str(event.code)
        check = True
        while check:
            chosen = int(input("What will you do?: "))
            if chosen:
                if chosen == 1 or chosen == 2 or chosen == 3 or chosen == 4:
                    check = False
                else:
                    print("Nonexistent action")
            else:
                print("Error")
                return
        method_name = f'event_{a}'
        obj = EventMethods(self.player,event)
        method = getattr(obj, method_name, None)
        if method:
            method(chosen)

class EventMethods:
    def __init__ (self,player,event):
        self.player = player
        self.event = event

    def event_1(self,choice):
        check = 1
        chosen = choice
        while check:
            if chosen == 1:
                self.player.damage(10)
                check = 0
            else:
                if chosen == 2:
                    check = 0
                else:
                    print("Nonexistent action")
                    chosen = int(input("What will you do?: "))
        print(self.event.getChoiceById(chosen).description)









