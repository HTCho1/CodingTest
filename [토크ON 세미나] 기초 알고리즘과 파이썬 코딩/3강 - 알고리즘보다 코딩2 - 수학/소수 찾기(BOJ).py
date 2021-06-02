'''
# O(N)
def isPrime(N):
    N = int(N)
    if N == 1: return False
    for i in range(2, N):
        # N이 i로 나누어 떨어지면 소수가 아니므로 False 반환
        if N % i == 0: return False
    # i를 N - 1까지 반복하는 동안,
    # N을 나눈 나머지가 0이 되는 i가 없으면 소수이므로 True 반환
    return True 

'''

# O(sqrt(N))
def isPrime(N):
    N = int(N)
    i = 2
    if N == 1: return False
    while i * i <= N:
        # N이 i로 나누어 떨어지면 소수가 아니므로 False 반환
        if N % i == 0: return False
        i += 1
    # i * i가 N까지 반복될 동안,
    # N을 나눈 나머지가 0이 되는 i가 없으면 소수이므로 True 반환
    return True

input()
l = list(map(isPrime, input().split())).count(True)
print(l)