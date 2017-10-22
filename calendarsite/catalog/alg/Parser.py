import Planner
import Event
import Homework
import datetime
import Exam


class parser:

    def __init__(self, arr):
        events = []
        tasks = []
        exams = []
        i = 0
        while (i < len(arr)):
            s = arr[i]
            if s == 'event':
                start = self._parsestringtodate(arr[i + 1])
                end = self._parsestringtodate(arr[i + 2])
                name = arr[i + 3]
                i+= 4
                events.append(Event.event(start, end, name))
            elif s == 'task':
                name = arr[i + 1]
                duration = int(arr[i + 2])
                time = self._parsestringtodate(arr[i + 3])
                i += 4
                tasks.append(Homework.homework(time, duration, name))
            else:
                name = arr[i + 1]
                duration = int(arr[i + 2])
                time = self._parsestringtodate(arr[i + 3])
                i += 4
                tasks.append(Exam.exam(time, duration, name))
        p = Planner.planner(events, tasks, exams)
        self.events = p.events


def _parsestringtodate(self, s):
        '''mm/dd/yyyy hh:mm'''
        m = int(s[:2])
        d = int(s[3:5])
        y = int(s[6:10])
        h = int(s[11:13])
        mi = int(s[13:15])
        return datetime.datetime(y, m, d, h, mi)

