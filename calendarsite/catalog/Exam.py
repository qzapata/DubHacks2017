import HomeworkSegment

class exam:


    IDEAL_WORK = 50
    IDEAL_BREAK = 15

    def __init__(self, date, studytime, name):
        self.date = date
        self.time = studytime
        self.name = name

    def intoChunks(self):
        eventList = []
        dur = self.time * 60
        while (dur > 0):
            if (dur > self.IDEAL_WORK):
                eventList.append(HomeworkSegment.homeworksegment(self.IDEAL_WORK, self.name))
                dur -= self.IDEAL_WORK
            else:
                eventList.append(HomeworkSegment.homeworksegment(dur, self.name))
                break
        return eventList