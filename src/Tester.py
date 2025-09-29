import json

from Classes import Player

a = Player("Micheal",100)

with open ("db.json","w") as file:
    json.dump(a.to_dict(),file,indent=4)
