import Planner
import Event
import Homework
import datetime

date = datetime.datetime.today()
da = datetime.date.today()
y = date.year
m = date.month
d = date.day

events = [Event.event(datetime.datetime(y, m, d, 0, 0), datetime.datetime(y, m, d, 9, 0), 'SleepMorning'),
          Event.event(datetime.datetime(y, m, d, 23, 0), datetime.datetime(y, m, d, 23, 59), 'SleepNight'),
          Event.event(datetime.datetime(y, m, d, 12, 0), datetime.datetime(y, m, d, 1, 30), 'Lunch'),
          Event.event(datetime.datetime(y, m, d, 16, 0), datetime.datetime(y, m, d, 18, 0), 'Lab'),
          Event.event(datetime.datetime(y, m, d + 1, 0, 0), datetime.datetime(y, m, d, 9, 0), 'SleepMorning'),
          Event.event(datetime.datetime(y, m, d + 1, 23, 0), datetime.datetime(y, m, d, 23, 59), 'SleepNight'),
          Event.event(datetime.datetime(y, m, d + 1, 11, 0), datetime.datetime(y, m, d, 12, 0), 'Lunch'),
          Event.event(datetime.datetime(y, m, d + 1, 18, 0), datetime.datetime(y, m, d, 20, 0), 'Dance'),
          Event.event(datetime.datetime(y, m, d + 2, 0, 0), datetime.datetime(y, m, d, 9, 0), 'SleepMorning'),
          Event.event(datetime.datetime(y, m, d + 2, 23, 0), datetime.datetime(y, m, d, 23, 59), 'SleepNight'),
          ]

homeworks = [Homework.homework(datetime.datetime(y, m, d, 23, 59), 4, 'Math'), Homework.homework(datetime.datetime(y, m, d + 1, 23, 59), 7, 'CS'),
             Homework.homework(datetime.datetime(y, m, d + 2, 12, 0), 2, 'English')]

p = Planner.planner(events, homeworks)

for p in p.events:
    print(p.__str__())
