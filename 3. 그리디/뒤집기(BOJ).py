S = input()

a0 = S.split('0')
a1 = S.split('1')

# 리스트에서 빈 문자열인 원소 제거
# a0 = [a for a in a0 if a]
a0 = ' '.join(a0).split()
# a1 = [a for a in a1 if a]
a1 = ' '.join(a1).split()

if len(a0) < len(a1):
    print(len(a0))
else:
    print(len(a1))