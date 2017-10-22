from Queue import PriorityQueue
import datetime
import Event
import Homework
import HomeworkSegment
import CalendarSpace
import math


class calendarmaker:

    IDEAL_HOUR = 19 * 60

    def __init__(self, homeworks, days):
        self.homeworks = homeworks
        self.days = days
        self.events = []
        for h in homeworks:
            duedate = datetime.date(h.dueDate.year, h.dueDate.month, h.dueDate.day)
            dates = []
            dateidx = 0
            while True:
                dates.append(days[dateidx])
                if days[dateidx].date == duedate:
                    break
                dateidx += 1
            cal = CalendarSpace.calendarspace(dates)
            newevents = self.getEvents(cal, h)
            for n in newevents:
                self.events.append(n)

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
            events.append(Event.event(e[0], e[0] + t, homework.name))
        return events

    def __str__(self):
        s = ''
        for e in self.events:
            s += e.__str__()
        return s

