# 피보나치 함수를 재귀 함수로 표현
def fibo(num):
    if num == 1 or num == 2:
        return 1
    return fibo(num - 1) + fibo(num - 2)

print(fibo(7))