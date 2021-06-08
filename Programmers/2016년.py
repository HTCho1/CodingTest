import sys
import datetime
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

def solution(a, b):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return days[datetime.date(2016, a, b).weekday()]

print(solution(a, b))

#--------------------------------------------------------------#

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

def solution(a, b):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    now = 4 # 금요일에 days index를 맞추기 위해 4를 더한다.
    for i in range(0, a - 1):
        now += month[i]

    answer = (now + b - 1) % 7

    return days[answer]

print(solution(a, b))

#---------------------------------------------------------------#
import sys

a, b = int(sys.stdin.readline()), int(sys.stdin.readline())

def getDayName(a,b):
    days=['FRI','SAT','SUN','MON','TUE','WED','THU']
    month=[31,29,31,30,31,30,31,31,30,31,30,31]

    return days[(sum(month[:a-1])+(b-1))%7]

print(getDayName(a,b))