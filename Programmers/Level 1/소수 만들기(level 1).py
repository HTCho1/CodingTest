# 프로그래머스 Level 1
# 소수 만들기, Summer/Winter Coding(~2018)

import sys
from itertools import combinations

nums = list(map(int, sys.stdin.readline().split()))

def solution(nums):
    nums.sort()
    comb = list(combinations(nums, 3))
    lst = []
    for i in comb:
        result = sum(i)
        lst.append(isPrime(result))
    return lst.count(True)

def isPrime(N):
    i = 2
    while i * i <= N:
        if N % i == 0: return False
        i += 1
    return True

print(solution(nums))

#-----------------------------------------------------------#

nums = list(map(int, sys.stdin.readline().split()))

def solution(nums):
    answer = 0
    comb = list(combinations(nums, 3))
    for i in comb:
        sum_num = sum(i)
        for j in range(2, sum_num):
            if sum_num % j == 0: break
        else:
            answer += 1
    return answer

print(solution(nums))