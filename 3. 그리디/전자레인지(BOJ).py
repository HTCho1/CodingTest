t = int(input())

buttons = [300, 60, 10]

count = [0, 0, 0]

for i in range(len(buttons)):
    count[i] += t // buttons[i]
    t %= buttons[i]

if t % buttons[2]:
    print('-1')
else:
    print(count[0], count[1], count[2])

#----------------------------------------------#

t = int(input())

if t % buttons[2]:
    print('-1')
else:
    A = t // 300
    B = (t % 300) // 60
    C = (t % 60) // 10
    print(A, B, C)