n = int(input())
P = list(map(int, input().split()))

P.sort()

result = 0
acc = list()

# P에 있는 원소들의 누적합을 계산하고
# 새로운 리스트에 추가한다.
for i in range(len(P)):
    result = result + P[i]
    acc.append(result)

print(sum(acc))

#--------------------------------------------#

from itertools import accumulate

n = int(input())
P = list(map(int, input().split()))

P.sort()

result = list(accumulate(P))

print(sum(result))