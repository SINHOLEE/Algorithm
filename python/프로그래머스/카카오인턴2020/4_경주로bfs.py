from collections import deque

def bfs():
    global answer, n, visited, dy, dx
    q = deque([])
    for i in range(4):
        ny, nx = dy[i], dx[i]
        if not (0 <= ny < n and 0 <= nx < n):
            continue
        if bod[ny][nx]:
            continue
        q.append((100, ny, nx, i))
        visited[ny][nx][0] = 100
    while q:
        cnt, y, x, d = q.popleft()

        if y == n-1 and x == n-1:
            answer = min(cnt, answer)
            continue
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if not (0 <= ny < n and 0 <= nx < n):
                continue
            if bod[ny][nx]:
                continue
            if k == d:
                visited[ny][nx][0] = cnt + 100

                q.append((cnt+100, ny, nx, k))
            else:
                if 0 < visited[ny][nx][0] < cnt + 600:
                    continue
                visited[ny][nx][0] = cnt + 600
                q.append((cnt+600, ny, nx, k))


def solution(board):
    global n, answer, visited, bod
    bod = board
    n = len(board[0])
    visited = [[[0,0] for _ in range(n)] for _ in range(n)]
    bfs()
    return answer


    #  우 좌 하 상
    #  0  1  2  3
dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)
visited = []
answer = 9999999999999999999999999999999
bod = []
n = 0
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 900)
print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]), 3800)
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]), 2100)
print(solution(	[[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]), 3200)
