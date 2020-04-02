import sys
input = sys.stdin.readline


def move():
    new_bucket = {}
    for k, items in bucket.items():
        r, c = k[0], k[1]
        s, d, z = items[0], items[1], items[2]

        # 기존의 상어 자리 지우기
        mat[r][c] = 0
        # del bucket[(r, c)]

        ny, nx = r + s*dy[d], c + s*dx[d]
        if d == 0 or d == 1:
            if (ny // (n - 1)) % 2:  # 홀수면 뒤에서 빼고
                ny = n - 1 - ny % (n - 1)
                d ^= 1
            else:  # 짝수면 그대로
                ny = ny % (n - 1)
        else:
            if (nx // (m - 1)) % 2:  # 홀수면 뒤에서 빼고
                nx = m - 1 - nx % (m - 1)
                d ^= 1
            else:  # 짝수면 그대로
                nx = nx % (m - 1)

        # 새로운 상어 자리 옮기기
        if new_bucket.get((ny, nx)) is not None:
            if new_bucket[(ny, nx)][2] < z:
                new_bucket[(ny, nx)] = (s, d, z)
        else:
            new_bucket[(ny, nx)] = (s, d, z)
            mat[ny][nx] = 1

    return new_bucket


def catch(x):
    y = 0
    for i in range(n):
        if bucket.get((y+i, x)) is not None:
            temp = bucket[(y+i, x)][2]
            del bucket[(y+i, x)]
            mat[y+i][x] = 0
            return temp
    return 0


dy = (-1, 1, 0, 0)
dx = (0, 0, 1, -1)
bucket = {}
n, m, nums = map(int, input().split())
mat = [[0] * m for _ in range(n)]
for _ in range(nums):
    r, c, s, d, z = map(int, input().split())
    bucket[(r-1, c-1)] = (s, d-1, z)
    mat[r-1][c-1] = 1

res = 0
for j in range(m):
    res += catch(j)
    bucket = move()
print(res)
