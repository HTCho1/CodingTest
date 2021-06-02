def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

print(gcd(33, 60))

def gcd(a, b):
    ret = 0
    for i in range(min(a, b)):
        if i == 0: continue
        if a % i == 0 and b % i == 0:
            ret = i
    return ret

print(gcd(33, 60))

# 유클리드 호제법
# GCD(a, b) = GCD(b, a % b)

def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

print(gcd(33, 60))