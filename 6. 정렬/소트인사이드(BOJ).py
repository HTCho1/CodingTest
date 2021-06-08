import sys
N = sys.stdin.readline()

array = []
for i in N[:-1]:
    array.append(int(i))
array.sort(reverse=True)

for i in array:
    print(i, end='')