N, K = map(int, input().split())

A, B = sorted(list(map(int, input().split()))), sorted(list(map(int, input().split())), reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))

#-------------------------------------------------------------------------------------------------------#
#Quick Sort

N, K = map(int, input().split())

A, B = list(map(int, input().split())), list(map(int, input().split()))

def quick_sort(array, reverse=False):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    if reverse:
        left_side = [x for x in tail if x >= pivot]
        right_side = [x for x in tail if x < pivot]
        return quick_sort(left_side, reverse=True) + [pivot] + quick_sort(right_side, reverse=True)
    else:
        left_side = [x for x in tail if x < pivot]
        right_side = [x for x in tail if x >= pivot]
        return quick_sort(left_side) + [pivot] + quick_sort(right_side)

A, B = quick_sort(A), quick_sort(B, reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))