# 프로그래머스 Level 1
# K번째 수, 정렬 문제
array = [1, 5, 2, 6, 3, 7, 4]

commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for i in commands:
        start, end, check = i[0] - 1, i[1], i[2] - 1
        sort_array = sorted(array[start:end])
        answer.append(sort_array[check])
    return answer

print(solution(array, commands))

#------------------------------------------------------#

array = [1, 5, 2, 6, 3, 7, 4]

commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for start, end, check in commands:
        answer.append(sorted(array[start - 1:end])[check - 1])
    return answer

print(solution(array, commands))