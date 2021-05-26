n, k = map(int, input().split())

l = []

for i in range(n):
    coin = int(input())
    l.append(coin)

l.sort(reverse=True)

count = 0

for coin in l:
    count += k // coin
    k = k % coin

print(count)