from collections import deque

n, e, start_e = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(e):
    l = list(map(int, input().split()))
    graph[l[0]][l[1]] = 1
    graph[l[1]][l[0]] = 1


def dfs(v):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n + 1):
        if (visited[i] == 0 and graph[v][i] == 1):
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = False
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if (visited[i] == 1 and graph[v][i] == 1):
                queue.append(i)
                visited[i] = False

visited = [False] * (n + 1)

dfs(start_e)
print()
bfs(start_e)