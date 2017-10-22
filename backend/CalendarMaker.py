from Queue import PriorityQueue
import datetime
import Event
import Homework
import HomeworkSegment
import CalendarSpace
import math


class CalendarMaker:

    IDEAL_HOUR = 19 * 60

    def __init__(self, homeworks, days):
        self.homeworks = homeworks
        self.days = days
        self.events = []
        for h in homeworks:
            duedate = datetime.date(h.dueDate.year, h.dueDate.month, h.dueDate.day)
            dates = []
            dateidx = datetime.date.today()
            while True:
                dates.append(dateidx)
                if dateidx == duedate:
                    break
            cal = CalendarSpace(dates)
            self.events.append(self.getEvents(cal, h))

    def getPriority(self, homework, time):
        return math.fabs((time.hour * 60 + time.minute) - self.IDEAL_HOUR) + (homework.dueDate.day - time.day)*10

    def getEvents(self, calsp, homework):
        segs = homework.intoChunks()
        q = PriorityQueue()
        events = []
        for e in calsp.times:
            q.put_nowait((self.getPriority(homework, e[0]), e))
        for x in range(0, len(segs)):
            e = q.get_nowait()[1]
            while e[0] >= homework.dueDate:
                e = q.get_nowait()[1]
            t = datetime.timedelta(0, 0, 0, 0, e[1])
            events.append(Event(e[0], e[0] + t, homework.name))
        return events

