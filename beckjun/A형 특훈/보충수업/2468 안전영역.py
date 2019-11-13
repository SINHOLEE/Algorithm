
DEBUG = False
di = [0, 0, 1, -1]
dj = [1, -1, 0 ,0]

def bfs(i, j, rain):
    q = [(i, j)]
    visited[i][j] = 1
    while q:
        x, y = q.pop()

        for k in range(4):
            xx, yy = x+di[k], y+dj[k]
            if 0<=xx<n and 0<= yy < n:
                if mat[xx][yy] > rain:
                    if visited[xx][yy] == 0:
                        q.append((xx,yy))
                        visited[xx][yy] = 1


n = int(input())

mat = [list(map(int, input().split())) for _ in range(n)]
max_height = max(sum(mat, []))

max_cnt = 1
for rain in range(1, max(sum(mat, []))):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and mat[i][j] > rain:
               cnt += 1
               bfs(i, j, rain)

    max_cnt = max(max_cnt, cnt)
    if DEBUG:
        print(rain, cnt)
        for line in visited:
            print(line)
print(max_cnt)