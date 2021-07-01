import sys
import heapq

n, m, start = map(int, sys.stdin.readline().rstrip().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
# C에서 다른 도시로 가는데 걸리는 시간을 저장할 리스트
d = []
# C에서 보낸 메세지를 받는 도시의 개수
t = 0
for i in range(1, n + 1):
    if (distance[i] == INF) or (distance[i] == 0):
        continue
    d.append(distance[i])
    t += 1

if len(d) == 0:
    print(-1)
else:
    print(t, max(d))