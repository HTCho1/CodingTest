# 프로그래머스 Level 2
# 카펫
# https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    grid = brown + yellow
    # for i in range(1, grid + 1):
    for i in range(3, int(grid ** 0.5) + 1):
        if grid % i == 0:
            width, height = grid // i, i
            print(f'width: {width}, height: {height}')
            if (width - 2) * (height - 2) == yellow:
                return [width, height]


if __name__ == "__main__":
    inputs = [[10, 2], [8, 1], [24, 24]]
    results = [[4, 3], [3, 3], [8, 6]]

    for inp, res in zip(inputs, results):
        out = solution(inp[0], inp[1])
        if out == res:
            print('O')
        else:
            print('X')
