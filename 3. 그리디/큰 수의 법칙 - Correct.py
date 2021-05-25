n, m, k = map(int, input().split())

number = list(map(int, input().split()))

number.sort(reverse=True)

first = number[0]
second = number[1]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += first * count
result += second * (m - count)

print(result)