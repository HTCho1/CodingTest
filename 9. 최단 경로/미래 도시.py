# 플로이드 워셜 알고리즘 문제이다.
import sys

INF = int(1e9)

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, sys.stdin.readline().rstrip().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            #print(graph)

# 수행된 결과를 출력
distance = graph[1][K] + graph[K][X]

if distance >= INF:
    print("-1")
else:
    print(distance)