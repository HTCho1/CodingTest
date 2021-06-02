# 10진수(string)를 n진수(int)로 바꾸는 함수

def stoi(s, n):
    ret = 0
    l = len(s)
    for i in range(l): ret += int(s[i]) * n ** (l - i -1)
    return ret

result = stoi('10505', 10)
print(result)