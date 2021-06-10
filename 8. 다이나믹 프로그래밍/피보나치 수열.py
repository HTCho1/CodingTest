# 피보나치 함수를 재귀 함수로 표현
def fibo(num):
    if num == 1 or num == 2:
        return 1
    return fibo(num - 1) + fibo(num - 2)

print(fibo(100))
# 이 방식은 num이 커지면 커질수록 수행 시간이 기하급수적으로 늘어난다.
# O(2**N) N ==30이면 10억 가량의 연산을 수행해야 한다.