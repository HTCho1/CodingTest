num_list = []

for _ in range(9):
    n = int(input())
    num_list.append(n)

max_value = 0
max_index = 0

for i in range(len(num_list)):
    if max_value < num_list[i]:
        max_value = num_list[i]
        max_index = i + 1

print(max_value)
print(max_index)


#--------------------------------------#

num_list = [int(input()) for l in range(9)]
print(max(num_list))
print(num_list.index(max(num_list)) + 1)