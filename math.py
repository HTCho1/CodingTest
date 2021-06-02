import math


print(math.factorial(5)) # 5 팩토리얼을 출력

print(math.sqrt(7)) # 7의 제곱근을 출력

print(math.gcd(21, 14)) # 21과 14의 최대 공약수를 출력

print(math.pi) # 파이 출력
print(math.e) # 자연상수 e 출력

#-------------------------------------#

a, b = map(int, input().split())
gcd = math.gcd(a, b)
lcm = a * b / math.gcd(a, b)

print('최대 공약수: ', gcd)
print('최소 공배수: ', int(lcm))