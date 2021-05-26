x, y = map(int, input().split())

day = 0
monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

for i in range(x - 1):
    day = day + monthList[i]

day = (day + y) % 7

print(weekList[day])

#-----------------------------------------------------------------#
# calendar module 사용
import calendar

monthList = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
x, y = map(int, input().split())

day = calendar.weekday(2007, x, y)
print(monthList[day])

#-----------------------------------------------------------------#
# datetime module 사용
import datetime

x, y = map(int, input().split())
ans = datetime.date(2007, x, y)
print(ans.strftime("%a").upper())
