# 북 북동 동 남동 남 남서 서 북서
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]


def is_good_to_go(y, x, d, mat, n):
    while True:
        ny, nx = y + dy[d], x + dx[d]
        if not (0 <= ny < n and 0 <= nx < n):
            break
        if mat[ny][nx]==1:
            return False
        mat[ny][nx] = 2
        y, x = ny, nx
    return True


def check(y, x, mat, n):
    for d in range(8):
        if is_good_to_go(y, x, d, mat, n):
            continue
        else:
            return False
    return True


def fill_foot_print(yy, xx, mat, n):
    dummy_mat = [arr[:] for arr in mat]
    for d in range(8):
        y, x = yy, xx
        while True:
            ny, nx = y + dy[d], x + dx[d]
            if not (0 <= ny < n and 0 <= nx < n):
                break
            dummy_mat[ny][nx] = 2
            y, x = ny, nx
    return dummy_mat


def dfs(y, x, mat, n):
    if cnt == n:
        return 1
    res = 0
    for j in range(n):
        if not mat[y+1][j]:
            mat[y+1][j] = 1
            res += dfs(y, j, fill_foot_print(y+1, j, mat, n), cnt + 1, n)
            mat[y+1][j] = 0

    return res


def solution(n):
    mat = [[0] * n for _ in range(n)]
    res = 0

    res += dfs(-1, 0, mat, n)

    return res


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))

print(solution(9))

print(solution(10))

print(solution(11))

print(solution(12))
