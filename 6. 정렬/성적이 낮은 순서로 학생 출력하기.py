N = int(input())

array = []
for i in range(N):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student: student[1])

#array = [input().split() for _ in range(N)]
#for i in array:
#    i[1] = int(i[1])
#def setting(data):
#    return data[1]
#array = sorted(info, key=setting)

for i in array:
    print(i[0], end=' ')

#------------------------------------------------#

N = int(input())

array = []
for i in range(N):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')