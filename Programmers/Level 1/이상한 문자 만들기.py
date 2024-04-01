# 프로그래머스 Level 1
# 이상한 문자 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    count = 0
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ':
            count = 0
            continue
        else:
            if count % 2 == 0:
                s[i] = s[i].upper()
            else:
                s[i] = s[i].lower()
            count += 1
    return ''.join(s)


if __name__ == "__main__":
    inputs = "try hello world"
    outputs = "TrY HeLlO WoRlD"
    result = solution(inputs)

    if result == outputs:
        print('O')
    else:
        print('X')
