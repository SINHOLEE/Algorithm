from itertools import combinations, permutations

n = 9
c = 0
for perm in permutations(range(n), n):
    c+= 1
    print(perm, c)

