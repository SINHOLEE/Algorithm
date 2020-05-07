def solution(board):
        # 상 우 하 좌
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    n = len(board)
    visited = [[[0,0,0,0] for _ in range(n)] for _ in range(n)]

            #cnt, d, y, x * 2
    queue = [(0, 1, 0, 0), (0, 3, 0, 1)]
    visited[0][0][1] = 1  # 우
    visited[0][1][3] = 1  # 좌
    answer = 0
    while queue:

        cnt, d, y, x = queue.pop(0)
        if (0 <= y+dy[d] < n and 0 <= x+dx[d] < n) and (y+dy[d] == n-1 and x+dx[d] == n-1):
            break
        if y == n-1 and x == n-1:
            break
        for k in range(4):
            ny, nx = y+dy[k], x+dx[k]
            if d == k or (d+2) % 4 == k:  ## 앞 뒤 이동
                if not (0 <= ny < n and 0 <= nx < n):
                    continue
                if board[ny][nx]:
                    continue
                if visited[ny][nx][d]:
                    continue
                visited[ny][nx][d] = 1
                queue.append((cnt+1, d, ny, nx))

            else:  # 90도 회전
                if not (0 <= ny < n and 0 <= nx < n):
                    continue
                if not (0 <= ny+dy[d] < n and 0 <= nx+dx[d] < n):
                    continue
                if board[ny][nx] or board[ny+dy[d]][nx+dx[d]]:
                    continue
                if visited[y][x][k] == 0:
                    visited[y][x][k] = 1
                    queue.append((cnt+1, k, y, x))
                if visited[y+dy[d]][x+dx[d]][k] == 0:
                    visited[y+dy[d]][x+dx[d]][k] = 1
                    queue.append((cnt+1, k, y+dy[d], x+dx[d]))
        answer = cnt
    return answer


solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]])
