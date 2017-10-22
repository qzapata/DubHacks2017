import CalendarMaker
import datetime
import Day

class planner:

    def __init__(self, events, homeworks):
        cal = CalendarMaker.calendarmaker(homeworks, self._getdays(events, homeworks))
        self.events = cal.events

    def _getdays(self, events, homeworks):
        lastday = self.getlastday(events, homeworks)
        d = {}
        didx = datetime.date.today()
        while (True):
            d[didx] = []
            if (didx == lastday):
                break
            didx += 1
        for e in events:
            edate = datetime.date(e.start.year, e.start.month, e.start.day)
            d[edate].append(e)
        days = []
        for t in d.keys():
            days.append(Day.day(d[t], t))
        return days

    def _getlastday(self, events, homeworks):
        lastday = datetime.date.today()
        for e in events:
            d = datetime.date(e.start.year, e.start.month, e.start.day)
            if (d > lastday):
                lastday = d
        for h in homeworks:
            d = datetime.date(h.dueDate.year, h.dueDate.month, h.dueDate.day)
            if (d > lastday):
                lastday = d
        return lastday