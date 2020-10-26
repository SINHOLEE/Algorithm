def draw(arr, mat):
    x1, y1, x2, y2 = arr
    x1 += 500
    x2 += 500
    y1 += 500
    y2 += 500
    for x in range(x1, x2+1):
        mat[y1][x] = 1
        mat[y2][x] = 1
    for y in range(y1, y2+1):
        mat[y][x1] = 1
        mat[y][x2] = 1
    return mat


def bfs(y, x, visited, mat):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    visited[y][x] = 1
    q = [(y, x)]

    while  q:
        y, x q.pop(0)
        for k in range(4):
            ny, nx = y+dy[k], x+dx[k]
            if not (0<=ny<1001 and 0<=nx<1001):
                continue
            if visited[ny][nx]:
                continue
            if mat[ny][nx]:
                visited[ny][nx] = 1
                q.append((ny, nx))
    return visited

def solution(n, squares):
    mat = [[0] * 1001 for _ in range(1001)]
    visited = [[0] * 1001 for _ in range(1001)]
    for square in squares:
        mat = draw(square, mat)
    res = 0
    for y in range(1001):
        for x in range(1001):
            if mat[y][x] and not visited[y][x]:
                res += 1
                visited = bfs(y, x, visited, mat)


if __name__ == "__main__":
    n = int(input())
    squares = [[*map(int, input().split())] for _ in range(n)]
    print(solution(n, squares))
