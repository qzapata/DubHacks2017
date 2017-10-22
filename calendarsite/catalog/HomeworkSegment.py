class homeworksegment:
    def __init__(self, time, name):
        self.time = time
        self.name = name

    def __str__(self):
        return self.time.__str__() + self.name
