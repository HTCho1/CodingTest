# BOJ 2644
N = int(input())

A, B = map(int, input().split())
parents = [0 for _ in range(N + 1)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    parents[y] = x

#print(parents)

Aa, Ba = [], []
Ad, Bd = 0, 0

while A > 0:
    Aa.append((A, Ad))
    Ad += 1
    A = parents[A]
#print(Aa)

while B > 0:
    Ba.append((B, Bd))
    Bd += 1
    B = parents[B]
#print(Ba)

for i in Aa:
    for j in Ba:
        if i[0] == j[0]: # 공통 조상이 있으면
            print(i[1] + j[1])
            exit()
print(-1)