# 프로그래머스 Level 1
# 체육복, 그리디 문제
import sys

n = int(sys.stdin.readline())
lost = list(map(int, sys.stdin.readline().split()))
reserve = list(map(int, sys.stdin.readline().split()))

def solution(n, lost, reserve):
    # 여벌의 체육복이 있는 학생(reserve)도 도난 당했을 수 있다고 하니까
    # reserve와 lost에 중복되는 값을 제거해주어야 한다.
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i - 1 in set_lost: # reserve 기준으로 왼쪽 lost 학생 먼저 빌려주는 것을 체크
            set_lost.remove(i - 1)
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)
    return n - len(set_lost)

print(solution(n, lost, reserve))

#------------------------------------------------------------------

import sys

n = int(sys.stdin.readline())
lost = list(map(int, sys.stdin.readline().split()))
reserve = list(map(int, sys.stdin.readline().split()))

def solution(n, lost, reserve):
    set_reserve = [r for r in reserve if r not in lost]
    set_lost = [r for r in lost if r not in reserve]
    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i - 1)
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)
    return n - len(set_lost)

print(solution(n, lost, reserve))