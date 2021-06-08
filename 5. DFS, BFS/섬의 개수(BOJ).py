# use DFS
import sys
sys.setrecursionlimit(10000)

def dfs(y, x):
    graph[y][x] = 0
    for i in range(len(dx)):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0 <= ny < h) and (0 <= nx < w) and graph[ny][nx] == 1:
            dfs(ny, nx)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i,j)
                count += 1
    print(count)

#--------------------------------------------------------------------#
# use DFS
import sys
sys.setrecursionlimit(10000)

def dfs(y, x):
    visited[y][x] = 1

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= -1 or ny <= -1 or nx >= w or ny >= h:
            continue
        if graph[ny][nx] == 1 and visited[ny][nx] == 0:
            dfs(ny, nx)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph, lands, visited = [], [], [[0 for _ in range(w)] for _ in range(h)]
    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]

    count = 0

    for i in range(h):
        raw = list(map(int, input().split()))
        for j in range(w):
            if raw[j] == 1:
                lands.append([i, j]) # 1이 있는 좌표(y,x)를 lands에 추가
        graph.append(raw)
    #print('graph: ', graph)
    #print('lands: ', lands)

    for land in lands:
        if visited[land[0]][land[1]] == 0:
            dfs(land[0], land[1])
            count += 1
    print(count)

#-----------------------------------------------------------------------------#
# use BFS
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        a, b = queue.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                queue.append((nx, ny))
                visited[nx][ny] = True
                graph[nx][ny] = False

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    dx = [-1, 1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, 1, -1, -1, 1]

    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)