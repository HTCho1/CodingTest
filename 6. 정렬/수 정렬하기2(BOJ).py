# BOJ 2751
import sys

N = int(sys.stdin.readline())

array = sorted([int(sys.stdin.readline()) for _ in range(N)])

for i in array:
    print(i)