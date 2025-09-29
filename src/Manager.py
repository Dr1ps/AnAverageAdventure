class Manager:
    functionMap = {
        "1A": event_1,
        "1B": event_2,
        "1C": event_3,
        "1D": event_4
        }
    def trigger(self,event):
        print(event.description)
        print(event.choices)
        a = str(event.code)+str(event.choices.code)
        self.functionMap[a]()

