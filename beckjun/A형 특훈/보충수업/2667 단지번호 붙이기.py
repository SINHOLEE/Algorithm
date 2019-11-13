n = int(input())

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
mat = [list(map(int, input())) for _ in range(n)]
# def DFS(x, y):
#     mat[x][y] = 0
#     ret = 0
#     for k in range(4):
#         if 0 <= x + di[k] < n and 0 <= y + dj[k] < n :
#             if mat[x + di[k]][y + dj[k]]:
#                 ret += DFS(x + di[k], y + dj[k])
#     return ret +1

def DFS(x, y):
    cnt = 1
    s=[(x, y)]
    mat[x][y] = 0
    while s:
        x, y = s.pop()
        for k in range(4):
            xx, yy = x + di[k], y+dj[k]
            if 0 <= xx < n and 0 <= yy < n:
                if mat[xx][yy]:
                    s.append((xx, yy))
                    mat[xx][yy] = 0
                    cnt+=1
    return cnt
# print(sum(mat,[]))
danji = []
for i in range(n):
    for j in range(n):
        if mat[i][j]:
            danji.append(DFS(i, j))

print(len(danji))
for i in sorted(danji):
    print(i)
