import datetime
import HomeworkSegment

class Homework:

    IDEAL_WORK = 50
    IDEAL_BREAK = 15

    def __init__(self, duedate, duration, name):
        self.dueDate = duedate
        self.duration = duration
        self.name = name

    def intoChunks(self):
        eventList = []
        dur = self.duration
        while (dur > 0):
            if (dur > self.IDEAL_WORK):
                eventList.append(HomeworkSegment(self.IDEAL_WORK, self.name))
                dur -= self.IDEAL_WORK
            else:
                eventList.append(HomeworkSegment(dur, self.name))
        return eventList

