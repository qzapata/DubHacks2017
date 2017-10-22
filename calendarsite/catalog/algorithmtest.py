import CalendarSpace
import CalendarMaker
import datetime
import Event
import Day
import Homework

date = datetime.datetime.today()
da = datetime.date.today()
y = date.year
m = date.month
d = date.day

events = [Event.event(datetime.datetime(y, m, d, 0, 0), datetime.datetime(y, m, d, 9, 0), 'SleepMorning'),
          Event.event(datetime.datetime(y, m, d, 23, 0), datetime.datetime(y, m, d, 23, 59), 'SleepNight'),
          Event.event(datetime.datetime(y, m, d, 12, 0), datetime.datetime(y, m, d, 1, 30), 'Lunch'),
          Event.event(datetime.datetime(y, m, d, 16, 0), datetime.datetime(y, m, d, 18, 0), 'Lab'),
          ]

homework = Homework.homework(datetime.datetime(y, m, d, 23, 59), 4, 'math pset')

day = Day.day(events, da)

calm = CalendarMaker.calendarmaker([homework], [day])

print(calm)
