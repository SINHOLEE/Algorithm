
di = [0,0,-1,1]
dj = [1,-1,0,0]
def delete_and_cnt():

    minus_mat = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if mat[i][j]:
                for k in range(4):
                    ii, jj = i+di[k], j+dj[k]
                    if 0 <= ii < r and 0 <= jj < c:
                        if mat[ii][jj] == 0:
                            minus_mat[i][j] += 1
    cnt = 0
    x = 0
    y = 0
    for i in range(r):
        for j in range(c):
            mat[i][j] -= minus_mat[i][j]
            if mat[i][j] > 0:
                cnt += 1
                x, y = i, j
            else:
                mat[i][j] = 0


    return x, y, cnt


def dfs(i, j):
    s = [(i, j)]
    visited = [[0] * c for _ in range(r)]
    visited[i][j] = 1
    cnt1 = 1
    while s:
        x, y = s.pop()
        for k in range(4):
            xx, yy = x+di[k], y+dj[k]
            if 0 <= xx < r and 0 <= yy < c:
                if visited[xx][yy] == 0 and mat[xx][yy] > 0:
                    visited[xx][yy] = 1
                    s.append((xx,yy))
                    cnt1 += 1
    return cnt1
r, c = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(r)]

year = 1
while True:

    x, y, cnt = delete_and_cnt()
    if cnt == 0:
        year = 0
        break

    t = dfs(x,y)
    if t != cnt:
        break
    year += 1

print(year)