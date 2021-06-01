n = int(input())

def solution(n):
    l, ret = len(str(n)), 0
    for i in range(1, l):
        ret += i * (10 ** i - 10 ** (i - 1))
    ret += l * (n - 10 ** (l - 1) + 1)
    return ret

result = solution(n)
print(result)

#---------------------------------------#

n = int(input())

result = 0
if 1 <= n <= 9:
    result = n
elif 10 <= n <= 99:
    result = (n * 2) - 9
elif 100 <= n <= 999:
    result = (n * 3) - 108
elif 1000 <= n <= 9999:
    result = (n * 4) - 1107
elif 10000 <= n <= 99999:
    result = (n * 5) - 11106
elif 100000 <= n <= 999999:
    result = (n * 6) - 111105
elif 1000000 <= n <= 9999999:
    result = (n * 7) - 1111104
elif 10000000 <= n <= 99999999:
    result = (n * 8) - 11111103
elif 100000000 <= n <= 999999999:
    result = (n * 9) - 111111102

print(result)

#---------------------------------------#

n = input()

result = 0
if len(n) == 1:
    result = n
elif len(n) == 2:
    result = (int(n) * 2) - 9
elif len(n) == 3:
    result = (int(n) * 3) - 108
elif len(n) == 4:
    result = (int(n) * 4) - 1107
elif len(n) == 5:
    result = (int(n) * 5) - 11106
elif len(n) == 6:
    result = (int(n) * 6) - 111105
elif len(n) == 7:
    result = (int(n) * 7) - 1111104
elif len(n) == 8:
    result = (int(n) * 8) - 11111103
elif len(n) == 9:
    result = (int(n) * 9) - 111111102

print(result)