d = [0] * 100

def fibo(num):
    print('f(' + str(num) + ')', end=' ')
    if num ==1 or num == 2:
        return 1
    if d[num] != 0:
        return d[num]
    d[num] = fibo(num - 1) + fibo(num - 2)
    return d[num]

print(fibo(8))