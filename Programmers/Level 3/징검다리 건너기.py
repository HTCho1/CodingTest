# 프로그래머스 Level 3
# 징검다리 건너기
# https://school.programmers.co.kr/learn/courses/30/lessons/64062
def check(stones, mid, k):
    skip = 0
    for stone in stones:
        if stone < mid:
            skip += 1
            if skip >= k:
                return 0
        else:
            skip = 0
    return 1


def solution(stones, k):
    answer = 0
    left, right = 0, max(stones)
    while left <= right:
        m = (left + right) // 2
        if check(stones, m, k):
            answer = m
            left = m + 1
        else:
            right = m - 1
    return answer


if __name__ == "__main__":
    inputs = [[2, 4, 5, 3, 2, 1, 4, 2, 5, 1]]
    kk = [3]
    results = [3]
    for stone, k, res in zip(inputs, kk, results):
        out = solution(stone, k)
        if out == res:
            print('O')
        else:
            print('X')
