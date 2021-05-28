# 8 X 8 체스판
k, s, n = input().split()
move_list = []
for i in range(int(n)):
    move_list.append(input())

dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
step_types = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']

king_column = int(ord(k[0])) - ord('A') + 1
king_row = int(k[1])
stone_column = int(ord(s[0])) - ord('A') + 1
stone_row = int(s[1])

for plan in move_list:
    # 이동 후 좌표 구하기
    for i in range(len(step_types)):
        if plan == step_types[i]:
            n_king_row = king_row + dx[i]
            n_king_column = king_column + dy[i]
            # 킹의 좌표가 체스판을 벗어나는 경우
            if n_king_row < 1 or n_king_column < 1 or n_king_row > 8 or n_king_column > 8:
                continue
            # 킹의 좌표와 돌의 좌표가 일치하는 경우, 돌 이동
            if n_king_row == stone_row and n_king_column == stone_column:
                n_stone_row = stone_row + dx[i]
                n_stone_column = stone_column + dy[i]
                # 돌의 좌표가 체스판을 벗어나는 경우
                if n_stone_row < 1 or n_stone_column < 1 or n_stone_row > 8 or n_stone_column > 8:
                    continue
                stone_row = n_stone_row
                stone_column = n_stone_column
            king_row = n_king_row
            king_column = n_king_column

king_column = chr(king_column + 64)
king_row = str(king_row)
stone_column = chr(stone_column + 64)
stone_row = str(stone_row)

print(king_column+king_row)
print(stone_column+stone_row)