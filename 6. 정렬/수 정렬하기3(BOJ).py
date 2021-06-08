# BOJ 10989
import sys

N = int(sys.stdin.readline())

count = [0] * 10001

for i in range(N):
    input_data = int(sys.stdin.readline())
    count[input_data] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)