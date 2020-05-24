dy = [0, -1]
dx = [-1, 0]


def bfs():
    global mat, target, n
    cnt = 0
    q = []
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        if mat[n-1][i]:
            visited[n-1][i] = 1
            q.append((n-1, i))
            cnt+=1
        if mat[i][n-1] and i != n-1:
            visited[i][n-1] = 1
            q.append((i, n-1))
            cnt+=1

    while q:
        y, x = q.pop(0)
        for k in range(2):
            ny, nx = y+dy[k], x+dx[k]
            if not(0<=ny<n and 0<=nx<n):
                continue
            if visited[ny][nx]:
                continue
            if mat[ny][nx] == 0:
                continue
            q.append((ny, nx))
            cnt+=1
            visited[ny][nx] = 1

    return "YES" if cnt == target else "NO"


t = int(input())

for i in range(t):
    n = int(input())
    mat = []
    for _ in range(n):
        temp = list(map(lambda x: int(x), list(input())))
        mat.append(temp)
    target = sum(sum(mat,[]))
    res = bfs()
    print(res)
