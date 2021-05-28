l = int(input())
s = list(map(int, input().split()))
n = int(input())

if n in s:
    print('0')
    exit()
s.sort()

result = 0
min_value = 0
max_value = 0

for i in s:
    if i < n:
        min_value = i
    if i > n:
        max_value = i
        break

for i in range(min_value + 1, max_value):
    if i > n:
        break
    for x in range(i + 1, max_value):
        print('i, x: ', i, ',', x)
        if i <= n <= x:
            result += 1
print(result)

#-------------------------------------------------------#

import sys


l = int(sys.stdin.readline())
lucky = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
if x in lucky:
    print(0)
    exit()
lucky.append(x)
lucky.sort()
a = lucky.index(x)
start = a - 1
stop = a + 1
if a == 0:
    cnt = (lucky[1] - lucky[0]) * lucky[0] - 1
else:
    cnt = (lucky[a] - lucky[start]) * (lucky[stop] - lucky[a]) - 1
print(cnt)