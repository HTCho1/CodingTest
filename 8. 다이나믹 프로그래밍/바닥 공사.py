# 점화식: a[i] = a[i - 1] + a[i - 2] * 2
import sys

n = int(sys.stdin.readline().rstrip())

d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d)
print(d[n])