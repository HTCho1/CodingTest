# 기본 정렬 라이브러리
N = int(input())

array = [int(input()) for _ in range(N)]

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')

# Selection Sort

N = int(input())

lst = [int(input()) for _ in range(N)]

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

for i in lst:
    print(i, end=' ')

# Insertion Sort
N = int(input())

lst = [int(input()) for _ in range(N)]

for i in range(1, len(lst)):
    for j in range(i, 0, -1):
        if lst[j] > lst[j - 1]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
        else:
            break

for i in lst:
    print(i, end=' ')

# Pythonic Quick Sort
N = int(input())

lst = [int(input()) for _ in range(N)]

def quick_sort(array):
    if len(array) == 1:
        return array

    pivot = array[0]
    l = array[1:]
    left_side = [x for x in l if x > pivot]
    right_side = [x for x in l if x <= pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

lst = quick_sort(lst)

for i in lst:
    print(i, end=' ')

# Quick Sort
N = int(input())

lst = [int(input()) for _ in range(N)]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] >= array[pivot]:
            left += 1
        while right > start and array[right] <= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(lst, 0, len(lst) - 1)
for i in lst:
    print(i, end=' ')

# Count Sort
N = int(input())

array = [int(input()) for _ in range(N)]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[lst[i]] += 1

for i in range(len(count) - 1, 0, -1):
    for j in range(count[i]):
        print(i, end=' ')
