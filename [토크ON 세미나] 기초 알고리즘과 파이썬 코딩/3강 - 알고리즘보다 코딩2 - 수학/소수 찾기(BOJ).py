'''
# O(N)
def isPrime(N):
    N = int(N)
    if N == 1: return False
    for i in range(2, N):
        if N % i == 0: return False
    return True 

'''

# O(sqrt(N))
def isPrime(N):
    N = int(N)
    i = 2
    if N == 1: return False
    while i * i <= N:
        if N % i == 0: return False
        i += 1
    return True

input()
l = list(map(isPrime, input().split())).count(True)
print(l)