import CalendarMaker
import datetime
import Day
from Queue import PriorityQueue

class planner:

    MONTH_VALUES = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    LEAP_VALUES = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    def __init__(self, events, homeworks, exams):
        sortedhw = self._sorthomework(homeworks)
        cal = CalendarMaker.calendarmaker(sortedhw, self._getdays(events, sortedhw, exams))
        self.events = cal.events

    def _getdays(self, events, homeworks, exams):
        lastday = self._getlastday(events, homeworks, exams)
        d = {}
        didx = datetime.date.today()
        while (True):
            d[didx] = []
            if (didx == lastday):
                break
            didx = datetime.date(didx.year, didx.month, didx.day + 1)
        for e in events:
            edate = datetime.date(e.start.year, e.start.month, e.start.day)
            d[edate].append(e)
        days = []
        for t in d.keys():
            days.append(Day.day(d[t], t))
        return days

    def _getlastday(self, events, homeworks, exams):
        lastday = datetime.date.today()
        for e in events:
            d = datetime.date(e.start.year, e.start.month, e.start.day)
            if (d > lastday):
                lastday = d
        for e in exams:
            d = datetime.date(e.date.year, e.date.month, e.date.day)
            if (d > lastday):
                lastday = d
        for h in homeworks:
            d = datetime.date(h.dueDate.year, h.dueDate.month, h.dueDate.day)
            if (d > lastday):
                lastday = d
        return lastday

    def _sorthomework(self, homeworks):
        q = PriorityQueue()
        newhw = []
        for h in homeworks:
            q.put_nowait((self._datetimetoint(h.dueDate), h))
        while not (q.empty()):
            newhw.append(q.get_nowait()[1])
        return newhw

    def _datetimetoint(self, date):
        if (date.year % 4 == 0):
            return (date.year * 525600 + (self._sumn(self.LEAP_VALUES, date.month) + date.day) * 1440 + date.hour * 60 + date.minute)
        return (date.year * 525600 + (self._sumn(self.MONTH_VALUES, date.month) + date.day) * 1440 + date.hour * 60 + date.minute)

    def _sumn(self, list, n):
        sum = 0
        i = 0
        while (i < n):
            sum += list[i]
            i += 1
        return sum



