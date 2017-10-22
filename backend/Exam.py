import HomeworkSegment

class exam:
    def __init__(self, date, studytime, name):
        self.date = date
        self.studytime = studytime
        self.name = name

    def intoChunks(self):
        eventList = []
        dur = self.studytime * 60
        while (dur > 0):
            if (dur > self.IDEAL_WORK):
                eventList.append(HomeworkSegment.homeworksegment(self.IDEAL_WORK, self.name))
                dur -= self.IDEAL_WORK
            else:
                eventList.append(HomeworkSegment.homeworksegment(dur, self.name))
                break
        return eventList