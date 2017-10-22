import datetime
import Event
from Queue import PriorityQueue

class day:

    def __init__(self, events, date):
        self.date = date
        self.events = self.sortEvents(events)

    def sortEvents(self, events):
        q = PriorityQueue()
        for e in events:
            q.put_nowait((e.getstartint(), e))
        newEvents = []
        while(not (q.empty())):
            newEvents.append(q.get_nowait()[1])
        return newEvents

    def __str__(self):
        s = ''
        for e in self.events:
            s += e.__str__()
        return self.date.__str__() + ' ' + s




