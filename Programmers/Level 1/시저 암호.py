# 프로그래머스 Level 1
# 시저 암호
# https://school.programmers.co.kr/learn/courses/30/lessons/12926
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        corr = ord('A') if s[i].isupper() else ord('a')
        s[i] = chr((ord(s[i]) - corr + n) % 26 + corr)

    return ''.join(s)


if __name__ == "__main__":
    inputs = [
        ("AB", 1),
        ("z", 1),
        ("a B z", 4),
    ]
    expected = [
        "BC",
        "a",
        "e F d",
    ]

    for (inp1, inp2), res in zip(inputs, expected):
        if solution(inp1, inp2) == res:
            print('O')
        else:
            print('X')
