dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n, m, r = map(int, input().split())

mat = [[*map(int, input().split())] for _ in range(n)]

def move():
    dummy_mat = [[0] * m for _ in range(n)]
    y, x = 0, 0

    while True:
        if dummy_mat[y][x]:
            return dummy_mat
        yy, xx = y, x
        for k in range(4):
            while True:
                yyy, xxx = yy + dy[k], xx + dx[k]
                if not (0 <= xxx < m and 0 <= yyy < n):
                    break
                if dummy_mat[yyy][xxx]:
                    break
                dummy_mat[yyy][xxx] = mat[yy][xx]
                yy, xx = yyy, xxx
        y+=1
        x+=1


for _ in range(r):
    mat = move()

for arr in mat:
    print(' '.join(map(str,arr)))