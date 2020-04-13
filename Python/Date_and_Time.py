# Problem 1 : Calendar Module

#Solution 1
import calendar
d,m,y = map(int,input().split())
print((calendar.day_name[calendar.weekday(y,d,m)]).upper())
____________________________________________________________________________________________________________________________________________
# Problem 2 : Time Delta

#Solution 1
from datetime import datetime as dt
fmt = "%a %d %b %Y %H:%M:%S %z"
for i in range(int(input())):
    print(int(abs((dt.strptime(input(), fmt) - dt.strptime(input(), fmt)).total_seconds())))
