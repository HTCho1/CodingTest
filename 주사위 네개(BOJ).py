n = int(input())

def money():
    d = sorted(list(map(int, input().split())))
    if len(set(d)) == 1:
        return d[0] * 5000 + 50000
    elif len(set(d)) == 2:
        if d[1] == d[2]: return d[2] * 1000 + 10000
        return 2000 + (d[1] + d[2]) * 500
    for i in range(3):
        if d[i] == d[i + 1]: return 1000 + d[i] * 100
    return max(d) * 100
print(max(money() for i in range(n)))

#-----------------------------------------------------------------#

n = int(input())

dices = [list(map(int, input().split())) for _ in range(n)]

def four_value(n):
    return 50000 + n * 5000
def three_value(n):
    return 10000 + n * 1000
def two_pairs_value(n1, n2):
    return 2000 + (n1 * 500) + (n2 * 500)
def two_value(n):
    return 1000 + n * 100
def no_value(n):
    return n * 100

l = [[0 for _ in range(6)] for _ in range(n)]
a = []
r_l = []
for i in range(n):
    for j in range(1, 7):
        count = dices[i].count(j)
        if count == 4:
            result = four_value(j)
            #print(result)
            r_l.append(result)
            break
        elif count == 3:
            result = three_value(j)
            #print(result)
            r_l.append(result)
            break
        elif count == 2:
            n1 = j
            for k in range(j + 1, 7):
                count_ = dices[i].count(k)
                if count_ == 2:
                    n2 = k
                    result = two_pairs_value(n1, n2)
                    r_l.append(result)
                    #print(result)
                    break
            result = two_value(n1)
            r_l.append(result)
            #print(result)
            break
        elif count == 1:
            a.append(j)
            max_value = max(a)
            result = no_value(max_value)
            r_l.append(result)
            #print(result)
print(max(r_l))