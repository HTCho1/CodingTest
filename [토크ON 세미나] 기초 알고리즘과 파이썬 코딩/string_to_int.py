# 10진수(string)를 n진수(int)로 바꾸는 함수

def stoi(s, n):
    ret = 0
    l = len(s)
    for i in range(l): ret += int(s[i]) * n ** (l - i -1)
    return ret

print(stoi('11', 2))

# 위 방식은 연산량이 많다.

def stoi(s, n):
    ret = 0
    for i in s: ret = ret * n + int(i)
    return ret

print(stoi('11', 2))