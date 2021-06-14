n, m = map(int, input().split())

array = [int(input()) for _ in range(n)]

d = [10001] * (m + 1)

print('array: ', array)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

print(d)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])