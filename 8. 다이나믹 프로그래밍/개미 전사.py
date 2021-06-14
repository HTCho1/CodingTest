# 점화식: a[i] = max(a[i - 1], a[i - 2] + k[i])
import sys

N = int(sys.stdin.readline().strip())

storage = list(map(int, sys.stdin.readline().rstrip().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍 (바텀업)
d[0] = storage[0]
d[1] = max(storage[0], storage[1])

for i in range(2, N):
    d[i] = max(d[i - 1], d[i - 2] + storage[i])

print(d)
print(d[N - 1])