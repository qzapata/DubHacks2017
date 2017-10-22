import datetime


class event:
    def __init__(self, start, end, name):
        self.start = start
        self.end = end
        self.name = name

    def getendint(self):
        return self.end.hour *60 + self.end.minute

    def getstartint(self):
        return self.start.hour * 60 + self.start.minute

    def __str__(self):
        return self.name + ' ' + self.start.__str__() + ' to ' + self.end.__str__()

