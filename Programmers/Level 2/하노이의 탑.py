# 프로그래머스 Level 2
# 하노이의 탑
# https://school.programmers.co.kr/learn/courses/30/lessons/12946
def hanoi(n, start, end, mid, a):
    if n == 1: return a.append([start, end])
    hanoi(n - 1, start, mid, end, a)
    a.append([start, end])
    hanoi(n - 1, mid, end, start, a)


def solution(n):
    a = []
    hanoi(n, 1, 3, 2, a)
    return a


if __name__ == "__main__":
    inputs = 2
    result = [[1, 2], [1, 3], [2, 3]]

    out = solution(inputs)
    if out == result:
        print('O')
    else:
        print('X')
