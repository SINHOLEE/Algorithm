import math


def dfs(y, x, d, cnt):
    global answer, n, visited, dy, dx

    if y == n - 1 and x == n - 1:
        answer = min(answer, cnt)
        return
    if cnt > answer:
        return
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if not (0 <= ny < n and 0 <= nx < n):
            continue
        if visited[ny][nx]:
            continue
        if bod[ny][nx]:
            continue
        if d == -1 or k == d:
            visited[ny][nx] = 1
            dfs(ny, nx, k, cnt + 100)
            visited[ny][nx] = 0
        else:
            visited[ny][nx] = 1
            dfs(ny, nx, k, cnt + 600)
            visited[ny][nx] = 0


def solution(board):
    global n, answer, visited, bod
    bod = board
    n = len(board[0])
    visited = [[0] * n for _ in range(n)]
    answer = math.inf
    visited[0][0] = 1
    dfs(0, 0, -1, 0)
    return answer


dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)
visited = []
answer = -1
bod = []
n = 0
solution(	[[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]])