import datetime
import Event

class Homework:

    IDEAL_WORK = 50
    IDEAL_BREAK = 15

    def __init__(self, duedate, duration):
        self.dueDate = duedate
        self.duration = duration
