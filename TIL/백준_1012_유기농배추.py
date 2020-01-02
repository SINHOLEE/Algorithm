import sys
input = sys.stdin.readline
T = int(input())
near = ((0, 1),(0, -1),(1, 0),(-1, 0))
def dfs(x,y):
    global cnt

    queue = [(x,y)]
    mat[x][y] = cnt
    while queue:
        x, y = queue.pop()

        for di, dj in near:
            newX, newY = x+di, y+dj
            if not (0<= newX < m and 0 <= newY < n):
                continue
            if mat[newX][newY] == -1:
                queue.append((newX,newY))
                mat[newX][newY] = cnt
    return 1
for t in range(T):
    n, m, k = map(int, input().split())

    mat = [[0] * n for _ in range(m)]
    for _ in range(k):
        a, b = map(int, input().split())
        mat[b][a] = -1
    cnt = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == -1:
                cnt += dfs(i,j)

    print(cnt)