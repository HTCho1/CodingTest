# 프로그래머스 Level 2
# h-index
# https://school.programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    citations = sorted(citations)
    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx:
            return len(citations) - idx
    return 0


if __name__ == "__main__":
    inputs = [[3, 0, 6, 1, 5],
              [10, 10],
              [2, 54, 7, 9, 10, 25, 3, 2, 2]]
    results = [3, 2, 5]

    for inp, res in zip(inputs, results):
        out = solution(inp)
        if out == res:
            print('O')
        else:
            print('X')
