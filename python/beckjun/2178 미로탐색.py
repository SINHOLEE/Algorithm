n, m = map(int, input().split())
mat = [input() for _ in range(n)]

dy = (1,-1, 0, 0)
dx = (0, 0, 1, -1)

visited = [[0] * m for _ in range(n)]
visited[0][0] = 1

q = [(1, 0, 0)]

while q:
    cnt, y, x = q.pop(0)
    if y == n-1 and x == m-1:
        print(cnt)
        break

    for k in range(4):
        ny, nx = y+dy[k], x+dx[k]
        if not (0<=ny<n and 0<= nx< m):
            continue
        if visited[ny][nx]:
            continue
        if mat[ny][nx] == '0':
            continue
        visited[ny][nx] = 1
        q.append((cnt+1, ny, nx))
