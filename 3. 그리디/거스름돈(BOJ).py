buy = int(input())

coins = [500, 100, 50, 10, 5, 1]

money = 1000
count = 0
change = money - buy

for coin in coins:
    count += change // coin
    change = change % coin

print(count)