nums = list(map(int, input().split()))

def solution(nums):
    c = len(nums) // 2
    nums_set = set(nums)
    if len(nums_set) >= c:
        answer = c
    else:
        answer = len(nums_set)
    return answer

print(solution(nums))