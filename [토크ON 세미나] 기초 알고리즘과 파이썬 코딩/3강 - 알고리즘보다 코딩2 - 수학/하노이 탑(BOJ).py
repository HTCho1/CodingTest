def hanoi(start, end, size):
    if size == 1: return print(start, end)
    # 1, 2, 3번 기둥의 합은 항상 6이다.
    # 6 - start - end를 하면 중간지점의 번호를 알 수 있다
    hanoi(start, 6 - start - end, size - 1)
    print(start, end)
    hanoi(6 - start - end, end, size - 1)

n = int(input())
print(2 ** n - 1)
hanoi(1, 3, n)