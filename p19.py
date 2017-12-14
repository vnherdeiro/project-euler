#! /usr/bin/python

import datetime

day = datetime.datetime(1901,1,1)
endDay = datetime.datetime(2000,12,31)
nSundays = 0
while day < endDay:
	if day.weekday() == 6 and day.day == 1:
		nSundays += 1
	day += datetime.timedelta(days=1)

print nSundays
