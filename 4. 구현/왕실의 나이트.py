coordinate = input()
row = int(coordinate[1])
column = int(ord(coordinate[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향
steps = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
count = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[1]
    next_column = column + step[0]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row < 1 or next_column < 1 or next_row > 8 or next_column > 8:
        continue
    count += 1

print(count)

#-----------------------------------------------------------------------#

coordinate = input()
row = int(coordinate[1])
column = int(ord(coordinate[0])) - int(ord('a')) + 1

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
count = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[1]
    next_column = column + step[0]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_column >= 1 and next_row <= 8 and next_column <= 8:
        count += 1

print(count)