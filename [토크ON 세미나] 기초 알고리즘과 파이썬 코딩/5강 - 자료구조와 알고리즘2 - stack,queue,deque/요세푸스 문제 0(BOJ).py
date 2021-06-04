# BOJ 11866
from collections import deque

N, k = map(int, input().split())

queue = deque(range(1, N + 1))
ans = list()

while len(queue):
    queue.rotate(-k + 1) # 원하는 k번째 숫자가 맨 앞으로 나오게 숫자를 rotate 해준다.
    ans.append(queue.popleft())

print(f'<{str(ans)[1:-1]}>')
#print('<{}>'.format(str(ans)[1:-1]))