# r, c = map(int, input().split())
#
# mat = [list(map(int, input().split())) for _ in range(r)]
# cctv = []
# for i in range(r):
#     for j in range(c):
#         if mat[i][j] != 0 and mat[i][j] != 6:
#             cctv.append(( i, j, mat[i][j]))
#
# print(cctv)


def fill_right(x, y, arr):
    yy = y + 1
    while yy < M and mat[x][yy] != 6:
        arr[x][yy] = 1
        yy += 1


def fill_left(x, y, arr):
    yy = y - 1
    while yy > -1 and mat[x][yy] != 6:
        arr[x][yy] = 1
        yy -= 1


def fill_up(x, y, arr):
    xx = x + 1
    while xx < N and mat[xx][y] != 6:
        arr[xx][y] = 1
        xx += 1


def fill_down(x, y, arr):
    xx = x - 1
    while xx > -1 and mat[xx][y] != 6:
        arr[xx][y] = 1
        xx -= 1


def observe():
    global ans
    tobserved = [arr[:] for arr in observed]

    for i in range(len(cctvXYC)):
        cctvC, x, y = cctvXYC[i]
        dir = direction[i]
        tobserved[x][y] = 1
        if cctvC == 1:
            if dir == 0:   fill_right(x, y, tobserved)
            elif dir == 1: fill_down(x, y, tobserved)
            elif dir == 2: fill_left(x, y, tobserved)
            elif dir == 3: fill_up(x, y, tobserved)
        elif cctvC == 2:
            if dir == 0:
                fill_right(x, y, tobserved)
                fill_left(x, y, tobserved)
            elif dir == 1:
                fill_up(x, y, tobserved)
                fill_down(x, y, tobserved)
        elif cctvC == 3:
            if dir == 0:
                fill_up(x, y, tobserved)
                fill_right(x, y, tobserved)
            elif dir == 1:
                fill_right(x, y, tobserved)
                fill_down(x, y, tobserved)
            elif dir == 2:
                fill_down(x, y, tobserved)
                fill_left(x, y, tobserved)
            elif dir == 3:
                fill_left(x, y, tobserved)
                fill_up(x, y, tobserved)
        elif cctvC == 4:
            if dir == 0:
                fill_right(x, y, tobserved)
                fill_left(x, y, tobserved)
                fill_up(x, y, tobserved)
            elif dir == 1:
                fill_right(x, y, tobserved)
                fill_down(x, y, tobserved)
                fill_up(x, y, tobserved)
            elif dir == 2:
                fill_right(x, y, tobserved)
                fill_down(x, y, tobserved)
                fill_left(x, y, tobserved)
            elif dir == 3:
                fill_down(x, y, tobserved)
                fill_left(x, y, tobserved)
                fill_up(x, y, tobserved)

    ans = max(ans, sum(sum(tobserved, [])))


def solve(k):
    global direction
    if k == len(cctvXYC):
        observe()
    else:
        if cctvXYC[k][0] == 2:
            for i in range(2):
                direction[k] = i
                solve(k + 1)
        else:
            for i in range(4):
                direction[k] = i
                solve(k + 1)


N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
observed = [[0] * M for i in range(N)]
cctvXYC = []

for x in range(N):
    for y in range(M):
        if mat[x][y] == 0 : continue
        elif mat[x][y] == 6:
            observed[x][y] = 1
        elif mat[x][y] == 5:
            observed[x][y] = 1
            fill_right(x, y, observed)
            fill_left(x, y, observed)
            fill_up(x, y, observed)
            fill_down(x, y, observed)
        else:
            cctvXYC.append((mat[x][y], x, y))

ans = 0
direction = [0] * len(cctvXYC)
solve(0)
print(N*M - ans)