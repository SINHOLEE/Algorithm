import sys
input = sys.stdin.readline

n = int(input())

mat = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
flag = False
for k in range(n):
    for u in range(n):
        for v in range(u+1, n):
            if u==k or v==k:
                continue
            if mat[u][v] > mat[u][k] + mat[k][v]:
                flag = True
            if mat[u][v] == mat[u][k] + mat[k][v]:
                visited[u][v] = 1
if flag:
    print(-1)
else:
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            if visited[i][j] == 0:
                res += mat[i][j]
    print(res)


