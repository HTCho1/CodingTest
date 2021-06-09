import sys

def binary_search(array, target, start, end):
    while start <= end:
        result = 0
        mid = (start + end) // 2
        for i in array:
            # 잘랐을 때의 떡의 양 계산
            if i > mid: # 떡의 높이가 절단기의 높이(mid)보다 작으면 자를 수 없기 때문에 큰 경우에만 절단
                result += i - mid
        if result == target:
            return mid
        elif result < target:
            end = mid - 1
        else:
            start = mid + 1
    return None

N, target = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))
array.sort()

print(binary_search(array, target, 0, max(array)))

#-----------------------------------------------------------------#
# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력
#n, m = list(map(int, input().split(' ')))
n, m = map(int, input().split())
# 각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total +=  x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)