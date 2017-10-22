import datetime
class Event:
    def __init__(self, start, end, name):
        self.start = start
        self.end = end
        self.name = name

    def getEndInt(self):
        return self.end.hour *60 + self.end.minute

    def getStartInt(self):
        return self.start.hour * 60 + self.start.minute

