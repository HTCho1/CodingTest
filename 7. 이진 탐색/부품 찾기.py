# 이진 탐색, 순차 탐색, 계수 정렬, 집합을 이용하여 4가지 방법으로 풀었음
import sys
# Binary Search
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 'yes'
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 'No'

n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))
array.sort() # 이진 탐색을 수행하기 위해 반드시 정렬을 수행해야 한다.
m = int(sys.stdin.readline().rstrip())
targets = list(map(int, sys.stdin.readline().rstrip().split()))

for target in targets:
    print(binary_search(array, target, 0, n - 1), end=' ')

#-------------------------------------------------------------------
# Sequential Search

def sequential_search(array, n, target):
    for i in range(n):
        if array[i] == target:
            return 'yes'
    return 'no'

n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
targets = list(map(int, sys.stdin.readline().rstrip().split()))

for i in targets:
    print(sequential_search(array, n, i), end=' ')

#-----------------------------------------------------------------------
# Count Sort (계수 정렬)

n = int(sys.stdin.readline().rstrip())
array = [0] * 1000001
for i in sys.stdin.readline().rstrip().split():
    array[int(i)] = 1
m = int(sys.stdin.readline().rstrip())
targets = list(map(int, sys.stdin.readline().split()))

for target in targets:
    # 해당 부품이 존재하는지 확인
    if array[target] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

#-------------------------------------------------------------------------
# Set (집합 자료형 이용)
n = int(sys.stdin.readline().rstrip())
array = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
targets = list(map(int, sys.stdin.readline().split()))

for target in targets:
    if target in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')