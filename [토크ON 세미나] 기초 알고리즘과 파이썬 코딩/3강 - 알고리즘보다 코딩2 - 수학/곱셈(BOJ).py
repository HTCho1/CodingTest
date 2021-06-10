# BOJ 1629
a, b, c = map(int, input().split())

def pow_custom(a, b, mod):
    ret = 1
    while b:
        if b % 2 == 1: ret = ret * a % mod
        # mod를 마지막에 나누는 것 보다 작은 수마다
        # 바로바로 나눠주는 것이 속도가 더 빠르다.
        a = a * a % mod
        b //= 2
    return ret

print(pow_custom(a, b, c))