# 프로그래머스 Level 1
# 콜라츠 추측
# https://school.programmers.co.kr/learn/courses/30/lessons/12943
def collatz(num, count):
    if num == 1: return count
    if count == 500: return -1
    if num % 2 == 0:
        return collatz(num // 2, count + 1)
    return collatz(num * 3 + 1, count + 1)


def solution(num):
    return collatz(num, 0)


if __name__ == "__main__":
    inputs = [6, 16, 626331]
    outputs = [8, 4, -1]

    for inp, out in zip(inputs, outputs):
        if solution(inp) == out:
            print('O')
        else:
            print('X')
