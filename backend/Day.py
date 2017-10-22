import datetime
import Event
from Queue import PriorityQueue

class Day:

    def __init__(self, events, date):
        self.events = events
        self.date = date
        self.sortEvents()

    def sortEvents(self):
        q = PriorityQueue()
        for e in self.events:
            q.put_nowait((e.getStartInt, e))
        newEvents = []
        while(not (q.empty())):
            newEvents.append(q.get_nowait())
        self.events = newEvents




