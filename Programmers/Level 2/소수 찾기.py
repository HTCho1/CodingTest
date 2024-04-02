# 프로그래머스 Level 2
# 소수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations


def is_prime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return 0
    return 1


def solution(num):
    a = set()
    num_list = list(num)
    for i in range(1, len(num_list) + 1):
        p = set(permutations(num_list, i))
        for j in p:
            num = int(''.join(j))
            if num < 2:
                continue
            if is_prime(num):
                a.add(num)
    return len(a)


if __name__ == "__main__":
    inputs = ["17", "011"]
    results = [3, 2]

    for inp, res in zip(inputs, results):
        out = solution(inp)
        if out == res:
            print('O')
        else:
            print('X')
