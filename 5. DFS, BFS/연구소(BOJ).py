from collections import deque
import copy

n, m = map(int, input().split())
max_num = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
empty_list = []
virus_list = []

EMPTY = 0
WALL = 1
VIRUS = 2

# 입력
graph = [[0] * m for _ in range(n)]

for x in range(n):
    raw = [int(x) for x in input().split()]
    for y in range(m):
        graph[x][y] = raw[y]
        if graph[x][y] == EMPTY:
            empty_list.append([x, y])
        if graph[x][y] == VIRUS:
            virus_list.append([x, y])

# bfs
def bfs(ng):
    queue = deque([])
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    global max_num

    for virus in virus_list:
        queue.append(virus)

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if ng[nx][ny] == EMPTY and visited[nx][ny] == False:
                queue.append([nx, ny])
                ng[nx][ny] = VIRUS
                visited[nx][ny] = True

    for i in range(n):
        cnt += ng[i].count(EMPTY)
    if max_num < cnt:
        max_num = cnt

# 벽 세우기
for i in range(len(empty_list)):
    for j in range(i):
        for k in range(j):
            x1, y1 = empty_list[i]
            x2, y2 = empty_list[j]
            x3, y3 = empty_list[k]

            graph[x1][y1] = WALL
            graph[x2][y2] = WALL
            graph[x3][y3] = WALL

            ng = copy.deepcopy(graph)
            bfs(ng)
            graph[x1][y1] = EMPTY
            graph[x2][y2] = EMPTY
            graph[x3][y3] = EMPTY

print(max_num)