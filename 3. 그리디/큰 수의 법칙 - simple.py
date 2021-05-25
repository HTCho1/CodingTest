# 단순하게 푸는 방식
n, m, k = map(int, input().split())
number = list(map(int, input().split()))

number.sort(reverse=True)

result = 0

first = number[0]
second = number[1]

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)