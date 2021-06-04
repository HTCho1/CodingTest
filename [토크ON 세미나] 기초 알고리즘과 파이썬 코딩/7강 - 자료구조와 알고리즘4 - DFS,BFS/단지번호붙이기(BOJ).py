# BOJ 2667
N = int(input())

A = []
for i in range(N):
    A.append(list(map(int, input())))
#A = [list(map(int, list(input()))) for _ in range(N)]
#    북  남 동  서
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ck = [[0 for _ in range(N)] for _ in range(N)]
c_lst = []

count = 0
def dfs(x, y):
    if x <= -1 or y <= -1 or x >= N or y >= N:
        return False
    ck[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <= -1 or ny <= -1 or nx >= N or ny >= N:
            return False
        if A[nx][ny] == 1 and ck[nx][ny] == 0:
            dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if A[i][j] == 1 and ck[i][j] == 0:
            dfs(i, j)
            count += 1
print(count)