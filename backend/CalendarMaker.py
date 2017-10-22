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
        for h in homeworks:
            duedate = datetime.date(h.dueDate.year, h.dueDate.month, h.dueDate.day)
            dates = []
            dateidx = datetime.date.today()
            while True:
                dates.append(dateidx)
                if dateidx == duedate:
                    break
            cal = CalendarSpace(dates)


    def getPriority(self, homework, time):
        return math.fabs((time.hour * 60 + time.minute) - self.IDEAL_HOUR) + (homework.dueDate.day - time.day)*10

    def getEvents(self, calsp, homework):
        segs = homework.intoChunks()
        q = PriorityQueue()
        for e in calsp.times:
            q.put_nowait(e)
