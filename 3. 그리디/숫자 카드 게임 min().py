n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    card = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_ = min(card)
    # '가장 작은 수' 중에서 가장 큰 수 찾기
    result = max(result, min_)

print(result)

#--------------------------------------------------#

result = 0

for i in range(n):
    card = list(map(int, input().split()))

    min_ = min(card)

    if result < min_:
        result = min_


print(result)
#######################################################

#--------------------------------------------------#

result = 0

for i in range(n):
    card = list(map(int, input().split()))
    card.sort()
    min_value = card[0]
    if result < min_value:
        result = min_value

print(result)