dy = [-1, 0, 1, 0] # 시계방향
dx = [0, 1, 0, -1]


def go(y, x, d, n, m, office):
    ny, nx = y+dy[d], x+dx[d]
    if not(0<= ny<n and 0<=nx<m):
        return y, x, d
    if office[ny][nx] == -1:
        return y, x, d
    return ny, nx, d


def turn(ord, y, x, d):
    if ord == 'right':
        d = (d+1) % 4
    else:
        d = (d+3) % 4
    return y, x, d


def solution(office, r, c, move):
    d = 0
    answer = 0
    n = len(office)
    m = len(office[0])
    for mov in move:
        if mov == 'go':
            r, c, d = go(r, c, d, n, m, office)
            answer += office[r][c]
            office[r][c] = 0
        else:
            r, c, d = turn(mov, r, c, d)
    return answer


print(solution([[5, -1, 4], [6, 3, -1], [2, -1, 1]], 1, 0, ["go", "go", "right", "go", "right", "go", "left", "go"]))
