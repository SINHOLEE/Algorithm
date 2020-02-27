dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def solution():
    for i in range(n):
        for j in range(m):
            if mat[i][j] == '.':
                for d in ('|', '-', '+', '1', '2', '3', '4'):
                    mat[i][j] = d
                    if check_method(i, j):
                        return str(i + 1), str(j + 1), d
                    mat[i][j] = '.'


def direction_method(target):
    # '|',  '-', '+', '1', '2', '3', '4
    if target == '|':
        return [0, 1]
    elif target == '-':
        return [2, 3]
    elif target == '+':
        return [0, 1, 2, 3]
    elif target == '1':
        return [1, 3]
    elif target == '2':
        return [0, 3]
    elif target == '3':
        return [0, 2]
    elif target == '4':
        return [1, 2]
    else:
        return []


# 답이 나온다면 True, 아니면 False 반환
def check_method(y, x):
    visited = [[[] for _ in range(m)] for _ in range(n)]
    visited[y][x] = direction_method(mat[y][x])
    q = [(y, x)]
    while q:
        yy, xx = q.pop(0)
        bucket = direction_method(mat[yy][xx])
        for dd in bucket:
            new_y, new_x = yy+dy[dd], xx+dx[dd]
            if not(0 <= new_y < n and 0 <= new_x < m):
                return False
            if mat[new_y][new_x] == '.':
                return False
            if mat[new_y][new_x] == 'M' or mat[new_y][new_x] == 'Z':
                visited[yy][xx].append(dd)
                continue
            if dd ^ 1 in visited[new_y][new_x]:
                continue
            if (dd ^ 1) in direction_method(mat[new_y][new_x]):
                visited[new_y][new_x].append(dd ^ 1)
                q.append((new_y, new_x))
            else:
                return False
            
    for i in range(n):
        for j in range(m):
            aa = sorted(direction_method(mat[i][j]))
            bb = sorted(visited[i][j])
            if aa != bb:
                return False
    return True


n, m = map(int, input().split())
mat = [list(input()) for _ in range(n)]
print(' '.join(solution()))
