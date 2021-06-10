# BOJ 1546
N = int(input())

scores = list(map(int, input().split()))

def average(N, array):
    r = 0
    for i in array:
        r += i / max(array) * 100
    return r / N

print(average(N, scores))