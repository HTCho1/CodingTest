# 시각 문제
# 완전 탐색 (Brute Forcing) 문제
# 하루는 86,400초이고 00시 00분 00초부터
# 23시 59분 59초 까지의 모든 경우는 86,400가지이다.

n = int(input())

count = 0
for i in range(n + 1):       # 시
    for j in range(60):      # 분
        for k in range(60):  # 초
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)