n, m = map(int, input().split())

result = 0

for i in range(n):
    card = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for j in range(m):
         min_value = min(min_value, card[j])
    # '가장 작은 수' 중에서 큰 수 찾기
    result = max(result, min_value)

print(result)

#------------------------------------------------#

result = 0

for i in range(n):
    card = list(map(int, input().split()))
    min_value = 10001
    for j in range(m):
        if min_value > card[j]:
            min_value = card[j]
    if result < min_value:
        result = min_value

print(result)