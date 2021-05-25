from itertools import permutations

data = ['A', 'B', 'C']

# 모든 순열 구하기
result = list(permutations(data, 3))

print('Permutations')
print(result)
print(len(result))

#------------------------------------------------#

from itertools import combinations

data = ['A', 'B', 'C']

# 2개를 뽑는 모든 조합 구하기
result = list(combinations(data, 2))

print('Combinations')
print(result)
print(len(result))

#-------------------------------------------------#

from itertools import product

data = ['A', 'B', 'C']

# 2개를 뽑는 모든 순열 구하기 (중복 허용)
result = list(product(data, repeat=2))

print('Product')
print(result)
print(len(result))

#--------------------------------------------------#

from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

# 2개를 뽑는 모든 조합 구하기 (중복 허용)
result = list(combinations_with_replacement(data, 2))

print('Combinations with replacement')
print(result)
print(len(result))