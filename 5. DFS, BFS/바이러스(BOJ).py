n = int(input())
edge = int(input())

line = [list(map(int, input().split())) for _ in range(edge)]
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in graph:
    graph[i[0]][i[1]] = graph[i[1]][i[0]] = 1

def dfs(v):
    visited[v] = True
    for i in range(1, n + 1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)

visited = [False] * (n + 1)
dfs(1)
print(visited.count(True) - 1)

#--------------------------------------------------#

n = int(input())
edge = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(edge):
    l = list(map(int, input().split()))
    graph[l[0]][l[1]] = graph[l[1]][l[0]] = 1

def dfs(v):
    visited[v] = True
    for i in range(1, n + 1):
        if (graph[v][i] == 1 and visited[i] == 0):
            dfs(i)

visited = [False] * (n + 1)
dfs(1)
print(visited.count(True) - 1)
