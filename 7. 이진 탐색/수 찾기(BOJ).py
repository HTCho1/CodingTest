# BOJ 1920
# Sequential Search -> 시간초과!! -> Binary Search로 구현해야 한다.
import sys
# 재귀함수를 이용한 binary search
def binary_search(array, target, start, end):
    if start > end:
        return '0'
    mid = (start + end) // 2
    if array[mid] == target:
        return '1'
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
targets = list(map(int, sys.stdin.readline().rstrip().split()))
array.sort()

for target in targets:
    print(binary_search(array, target, 0, n- 1))

#------------------------------------------------------------------
# 반복문을 이용한 binary search

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return '1'
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return '0'
