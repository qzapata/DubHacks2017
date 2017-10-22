import Planner
import Event
import Homework
import datetime


class parser:

    def __init__(self, arr):
        o = arr[0]
        events = o['event']
        tasks = o['task']
        exam = o['exam']
        e = self._getevents(events)
        t = self._gethw(tasks)
        p = Planner.planner(e, t)
        self.events = p.events

    def _getevents(self, events):
        e = []
        for d in events:
            start = self._parsestringtodate(d['time'])
            end = self._parsestringtodate(d['duedate'])
            name = d['name']
            e.append(start, end, name)
        return e

    def _gethw(self, tasks):
        h = []
        for d in tasks:
            time = int(d['time'])
            duedate = self._parsestringtodate(d['duedate'])
            name = d['name']
            h.append(duedate, time, name)
        return h

    def _parsestringtodate(self, s):
        '''mm/dd/yyyy hh:mm'''
        m = int(s[:2])
        d = int(s[3:5])
        y = int(s[6:10])
        h = int(s[11:13])
        mi = int(s[13:15])
        return datetime.datetime(y, m, d, h, mi)

