import Event
import datetime
import Homework


class CalendarSpace:

    DAY_TIME = 24*60
    IDEAL_WORK = 50
    IDEAL_BREAK = 15

    def __init__(self, days):
        self.times = []
        self.fillDates(days)

    def fillDates(self, days):
        for d in days:
            self.getDayTimes(d)

    def getDayTimes(self, day):
        timeidx = 0
        eventidx = 0
        while timeidx < self.DAY_TIME:
            if eventidx >= day.events.len():
                dur = self.IDEAL_WORK
                if timeidx + dur > self.DAY_TIME:
                    dur = self.DAY_TIME - timeidx
                self.times.append((datetime.datetime(day.date.year, day.date.month, day.date.date, timeidx / 60, timeidx % 60), dur))
                timeidx += self.IDEAL_WORK + self.IDEAL_BREAK
            else:
                if timeidx  + self.IDEAL_WORK < day.events[eventidx].getStartInt():
                    self.times.append((datetime.datetime(day.date.year, day.date.month, day.date.date, timeidx / 60,
                                                         timeidx % 60), dur))
                    timeidx += self.IDEAL_WORK + self.IDEAL_BREAK
                else:
                    timeidx = day.events[eventidx].getEndInt() + 15
                    eventidx += 1


