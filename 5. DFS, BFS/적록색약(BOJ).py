import sys
sys.setrecursionlimit(10**6)

n = int(input())

graph, visited = [list(map(str, input())) for _ in range(n)], [[0 for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x):
    visited[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n and graph[y][x] == graph[ny][nx] and visited[ny][nx] == 0:
            dfs(ny, nx)

# 적록색약이 아닌 경우
count_1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            count_1 += 1
            dfs(i, j)

# 적록색약인 경우
count_2 = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            count_2 += 1
            dfs(i, j)

print(count_1, count_2)