# BOJ 2839
N = int(input())

count = 0
while True:
    if N % 5 == 0:
        count += (N // 5)
        break
    count += 1
    N -= 3
    if N < 0:
        count = -1
        break

print(count)