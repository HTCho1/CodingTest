# 2부터 N - 1까지 체크
# 시간 복잡도가 O(N)
def isPrime(N):
    for i in range(2, N):
        if N % i == 0: return print('소수가 아닙니다.')
    return print('소수입니다.')

isPrime(1)


# 2부터 sqrt(N)까지 체크
# 시간 복잡도가 O(sqrt(N))
def isPrime(N):
    i = 2
    while i * i <= N:
        if N % i == 0: return print('소수가 아닙니다.')
        i += 1
    return print('소수입니다.')

isPrime(1)