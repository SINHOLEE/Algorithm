n, k = map(int, input().split())

mat = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    a, b = map(int,input().split())
    mat[a][b] = 1


for k in range(1, n+1):
    for i in range(1, n+1):
        if i == k:
            continue
        for j in range(1, n+1):
            if i == j:
                continue
            if mat[i][k] and mat[k][j]:
                mat[i][j] = 1

s = int(input())
res = []
for _ in range(s):
    a, b = map(int, input().split())

    one = mat[a][b]
    two = mat[b][a]
    if not (one or two):
        res += ['0']
    else:
        if one:
            res += ['-1']
        else:
            res += ['1']
for a in res:
    print(a)
