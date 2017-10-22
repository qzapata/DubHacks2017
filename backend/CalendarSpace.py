import Event
import datetime
import Homework
import math


class calendarspace:

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
            if eventidx >= len(day.events):
                dur = self.IDEAL_WORK
                if timeidx + dur > self.DAY_TIME:
                    dur = self.DAY_TIME - timeidx
                self.times.append((datetime.datetime(day.date.year, day.date.month, day.date.day, timeidx / 60, timeidx % 60), dur))
                timeidx += self.IDEAL_WORK + self.IDEAL_BREAK
            else:
                if timeidx + self.IDEAL_WORK < day.events[eventidx].getstartint():
                    self.times.append((datetime.datetime(day.date.year, day.date.month, day.date.day,
                                                         math.trunc(timeidx / 60), timeidx % 60), self.IDEAL_WORK))
                    timeidx += self.IDEAL_WORK + self.IDEAL_BREAK
                else:
                    timeidx = day.events[eventidx].getendint() + 15
                    eventidx += 1

    def __str__(self):
        s = ''
        for e in self.times:
            s += e[0].__str__() + ' for ' + str(e[1]) + ', '
        return s


