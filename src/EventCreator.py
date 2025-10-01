import json
from dataclasses import asdict
from typing import List

from Classes import Event, Choice, EventTime

inp = 1
if inp == 2:
    with open ("db.json","w") as file:
        json.dump([],file,indent=4)
else:
    if inp == 1:


        c1 = Choice("Eat it",1,"You ate the can of soup,"
                               "it was expired! Bleah!!!",10)
        c2 = Choice("Ignore it",2,"You ignored the soup, you thought"
                                  "about all the bugs you could find in it.",0)
        choices: List[Choice] = [c1,c2]
        e = Event(1,"You find a can of soup perfectly placed in the center"
                    "of a tree stump, it's half eaten and looks appealing.", EventTime(1).name,
                  choices)
        events: List[Event] = []

        with open ("db.json","r") as file:
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
        events.append(e)
        event_dicts = [asdict(k) for k in events]
        with open ("db.json","w") as file:
            json.dump(event_dicts,file,indent=4)