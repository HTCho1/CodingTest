k, s, n = input().split()
move_list = []
for i in range(int(n)):
    move_list.append(input())

steps = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, 1), (1, -1)]

king_row = int(ord(k[0])) - ord('A') + 1
king_column = int(k[1])
stone_row = int(ord(s[0])) - ord('A') + 1
stone_column = int(s[1])

for i in range(int(n)):
    next_king_row =