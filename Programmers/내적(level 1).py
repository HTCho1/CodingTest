# 프로그래머스 Level 1
# 내적, 월간 코드 챌린지 시즌1

a, b = list(map(int, input().split())), list(map(int, input().split()))

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer

print(solution(a, b))

#-------------------------------------------------------------------#

a, b = list(map(int, input().split())), list(map(int, input().split()))

def solution(a, b):
    return sum(x * y for x, y in zip(a, b))

print(solution(a, b))