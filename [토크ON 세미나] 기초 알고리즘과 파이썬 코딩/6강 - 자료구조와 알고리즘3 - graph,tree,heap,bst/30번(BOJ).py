# BOJ 13116
# Binary Tree 문제
def solution(a, b):
    while not a == b:
        if a > b: a //= 2
        else: b //= 2
    ret = a
    return ret

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    print(solution(a, b) * 10)

#----------------------------------------#

lst =list()
for i in range(T):
    lst.append(list(map(int, input().split())))

for i in lst:
    a, b = i[0], i[1]
    print(solution(a, b) * 10)