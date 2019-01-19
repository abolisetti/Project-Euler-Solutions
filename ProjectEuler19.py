#Project Euler 19

import datetime as dt
delta = dt.timedelta(days=1)

dow = 6 #Sunday
day = 1 #date
start_date = s = dt.datetime(1901, 1, 1)
end_date = dt.datetime(2000, 12, 31)

c = 0
while start_date <= end_date:
	if start_date.day==day and start_date.weekday()==dow: c+=1
	start_date += delta

print("Days on the 1st of the month between", s.strftime("%d-%b-%Y"), \
"\nand", end_date.strftime("%d-%b-%Y"), "inclusive:", c)
