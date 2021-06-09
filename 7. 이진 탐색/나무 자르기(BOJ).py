# BOJ 2805
# 시간 초과에 유의하여 문제를 풀어야 함
import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        length = 0
        for i in array:
            if i > mid:
                length += i - mid
            if length > target: # 이미 target보다 크면 더 루프를 돌 필요가 없으므로 빠져나감 -> 실행 시간 절약
                break
        if length < target:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer

n, target = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
answer = 0

print(binary_search(array, target, 0, max(array)))

#---------------------------------------------------------------

n, target = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))


start, end = 0, max(array)
answer = 0
while (start <= end):
    mid = (start + end) // 2
    total = 0
    for i in array:
        if i > mid:
            total += i - mid
        if total >= target: # 이미 target보다 크면 더 루프를 돌 필요가 없으므로 빠져나감 -> 시간 절약
            break
    if total < target:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)
