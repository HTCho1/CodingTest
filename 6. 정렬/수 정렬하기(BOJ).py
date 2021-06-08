# BOJ 2750
N = int(input())

array = [int(input()) for _ in range(N)]
array.sort()

for i in array:
    print(i)

#----------------------------------------------#
# Quick Sort
import sys
sys.setrecursionlimit(10000)

N = int(input())
array = [int(input()) for _ in range(N)]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

array = quick_sort(array)
for i in array:
    print(i)