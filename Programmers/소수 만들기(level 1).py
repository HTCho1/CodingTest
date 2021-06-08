# 프로그래머스 Level 1
# 소수 만들기, Summer/Winter Coding(~2018)

import sys
from itertools import combinations

nums = list(map(int, sys.stdin.readline().split()))

def solution(nums):
    nums.sort()
    comb = list(combinations(nums, 3))
    print(comb)
    answer = []
    for i in comb:
        print(i)
        result = sum(i)
        for j in range(2, result):
            if result % j != 0: answer.append(result)
    return len(answer)

print(solution(nums))