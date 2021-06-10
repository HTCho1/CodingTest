# BOJ 2588
a = int(input())
b = list(input())
three = a * int(b[-1])
four = a * int(b[-2])
five = a * int(b[-3])
total = three + (four * 10) + (five * 100)
print(three)
print(four)
print(five)
print(total)

#------------------------------------------------

num1 = int(input())
num2 = int(input())

a = num2 // 100
b = (num2 // 10) % 10
c = num2 % 10

r1 = num1 * c
r2 = num1 * b
r3 = num1 * a
result = r1 + (r2 * 10) + (r3 * 100)

print(r1)
print(r2)
print(r3)
print(result)