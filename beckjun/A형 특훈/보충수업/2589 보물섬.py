n, m = map(int, input().split())

mat = [list(input()) for i in range(n)]
di = [0, 0, 1, -1]
dj = [1,-1, 0, 0]

DEBUG=True
def bfs(i, j):
    visited = [[0] * m for _ in range(n)]
    q = []
    q.append((i, j, 0))
    cnt = 0
    visited[i][j] = 1
    while q:
        x, y, d = q.pop(0)
        for k in range(4):
            xx = x + di[k]
            yy = y + dj[k]
            if (0 <= xx < n and 0 <= yy < m) and visited[xx][yy] == 0 and mat[xx][yy] =='L':
                q.append((xx,yy, d+1))
                visited[xx][yy] = 1

        if DEBUG:
            print(x, y)
            for i in range(n):
                for j in range(m):
                    print(visited[i][j], end=" ")
                print()
            print(d)
            print()
    return d


max_dis = 0
for i in range(n):
    for j in range(m):
        if mat[i][j] == 'L':
            temp = bfs(i, j)
            if max_dis < temp:
                max_dis = temp
print(max_dis)
