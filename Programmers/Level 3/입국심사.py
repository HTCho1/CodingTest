# 프로그래머스 Level 3
# 입국심사
# https://school.programmers.co.kr/learn/courses/30/lessons/43238
def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break

        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


if __name__ == "__main__":
    persons = [6]
    times = [[7, 10]]
    results = [28]

    for person, time, res in zip(persons, times, results):
        print(person, time)
        out = solution(person, time)
        if out == res:
            print('O')
        else:
            print('X')
