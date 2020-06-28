def dfs(depth, p, y, x):
    global res
    if depth == n:
        res += p
        return

    for k in range(4):
        if arr[k] == 0:
            continue
        ny, nx = y+dy[k], x+dx[k]
        if visited[ny][nx]:
            continue
        visited[ny][nx] = 1
        dfs(depth+1, p * (arr[k] / 100), ny, nx)
        visited[ny][nx] = 0


dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
temp = list(map(int, input().split()))
n = temp[0]
arr = temp[1:]
N = 2 * n + 1
visited = [[0] * N for _ in range(N)]
visited[n][n] = 1
res = 0
dfs(0, 1, n, n)
print(res)
