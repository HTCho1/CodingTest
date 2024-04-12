# 프로그래머스 Level 2
# 수식 최대화
# https://school.programmers.co.kr/learn/courses/30/lessons/67257
from itertools import permutations


def split_num_oper(expression):
    num_list = []
    number = ''
    for idx, char in enumerate(expression):
        if not char.isdigit():
            num_list.append(number)
            num_list.append(char)
            number = ''
        else:
            number += char
        if idx == len(expression) - 1:
            num_list.append(number)
    return num_list


def solution(expression):
    answer = []
    for oper_permu in permutations(["-", "+", '*'], 3):
        num_list = split_num_oper(expression)
        for oper in oper_permu:
            while oper in num_list:
                idx = num_list.index(oper)
                num_list[idx - 1] = str(eval(''.join(num_list[idx-1:idx+2])))
                num_list[idx] = num_list[idx + 1] = ''
                num_list = [i for i in num_list if i]
        answer.append(abs(int(num_list[0])))
    return max(answer)


if __name__ == "__main__":
    inputs = ["100-200*300-500+20",
              "50*6-3*2"]
    results = [60420, 300]

    for inp, res in zip(inputs, results):
        out = solution(inp)
        if out == res:
            print('O')
        else:
            print('X')
