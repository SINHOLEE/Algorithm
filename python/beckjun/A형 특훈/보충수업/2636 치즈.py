di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def cheese(i, j):
    s = [(i, j)]
    visited[i][j] = 1
    while s:
        x, y = s.pop()
        for k in range(4):
            xx, yy = x+di[k], y + dj[k]
            if 0 <= xx < r and 0 <= yy < c:
                if visited[xx][yy] == 0 and mat[xx][yy] == 1 :
                    visited[xx][yy] = 1
                    s.append((xx,yy))

def outside(i, j):
    global outside_cheese_cnt
    s = [(i, j)]
    mat[i][j] = 3
    while s:
        x, y = s.pop()
        for k in range(4):
            xx, yy = x+di[k], y + dj[k]
            if 0 <= xx < r and 0 <= yy < c:
                if mat[xx][yy] == 1:
                    mat[xx][yy] = 2

                if mat[xx][yy] == 0:
                    mat[xx][yy] = 3
                    s.append((xx, yy))


r, c = map(int, input().split())

mat = [list(map(int,input().split())) for _ in range(r)]
year = 0
while sum(sum(mat, [])):

    visited = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if visited[i][j] == 0 and mat[i][j] == 1:
                cheese(i, j)
            if 1 <= i < r-1 and 1 <= j < c-1:
                continue
            if mat[i][j] == 0:
                outside(i, j) # 바깥공기를 3으로 바꾼다.

    year += 1
    outside_cheese_cnt = 0
    for i in range(r):
        for j in range(c):
            if mat[i][j] == 3:
                mat[i][j] = 0
            elif mat[i][j] == 2:
                mat[i][j] = 0
                outside_cheese_cnt += 1


print(year)
print(outside_cheese_cnt)