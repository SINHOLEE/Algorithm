def is_wall(y, x, n, m):
    return not (0 <= y < n and 0 <= x < m)


def is_fish_in_mat(y, x, mat):
    return 1 <= mat[y][x] <= 16


def fish_move(fish_idx, kk, new_fish_y, new_fish_x, fish_y, fish_x, fishes, mat):
    if is_fish_in_mat(new_fish_y, new_fish_x, mat):
        fishes[fish_idx][2] = kk
        observed_idx = mat[new_fish_y][new_fish_x]
        fishes[fish_idx], fishes[observed_idx] = fishes[observed_idx], fishes[fish_idx]
        fishes[fish_idx][2], fishes[observed_idx][2] = fishes[observed_idx][2], fishes[fish_idx][2]
        mat[fish_y][fish_x], mat[new_fish_y][new_fish_x] = mat[new_fish_y][new_fish_x], mat[fish_y][fish_x]
    else:
        fishes[fish_idx] = [new_fish_y, new_fish_x, kk]
        mat[fish_y][fish_x], mat[new_fish_y][new_fish_x] = mat[new_fish_y][new_fish_x], mat[fish_y][fish_x]


def game(shark_y, shark_x, shark_d, total, fishes, mat):
    global score
    score = max(total, score)
    # 2-1. 물고기가 먼저 움직인다.
    for fish_idx in range(1, 17):
        if not fishes[fish_idx]:
            continue
        fish_y, fish_x, fish_d = fishes[fish_idx]
        for k in range(8):
            kk = (k + fish_d) % 8
            new_fish_y, new_fish_x = fish_y + dy[kk], fish_x + dx[kk]
            if is_wall(new_fish_y, new_fish_x, 4, 4):
                continue
            elif mat[new_fish_y][new_fish_x] == 20:
                continue
            else:
                fish_move(fish_idx, kk, new_fish_y, new_fish_x, fish_y, fish_x, fishes, mat)
                break
                #
    # 2.2 물고기가 다 움직이면 상어가 움직인다.
    for times in range(1, 4):
        new_shark_y, new_shark_x = shark_y + times*dy[shark_d], shark_x + times*dx[shark_d]
        if is_wall(new_shark_y, new_shark_x, 4, 4):
            continue
        if is_fish_in_mat(new_shark_y, new_shark_x, mat):  # 상어가 먹을 물고기가 있다면,
            eaten_fish_idx = mat[new_shark_y][new_shark_x]
            eaten_y, eaten_x, eaten_d = fishes[eaten_fish_idx]  # dfs 데이터 관리시 필요
            mat[shark_y][shark_x] = 0
            fishes[eaten_fish_idx] = []
            mat[eaten_y][eaten_x] = 20

            # 2-3. 상어가 움직일 조건이면, 데이터 변환 후 dfs 탐색에 들어간다.
            game(
                new_shark_y,
                new_shark_x,
                eaten_d,
                total + eaten_fish_idx,
                [arr[:] for arr in fishes],
                [arr[:] for arr in mat]
            )

            fishes[eaten_fish_idx] = [eaten_y, eaten_x, eaten_d]
            mat[eaten_y][eaten_x] = eaten_fish_idx
            mat[shark_y][shark_x] = 20


dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
mat = [[0] * 4 for _ in range(4)]
fishes = [[] for _ in range(17)]
for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(4):
        d = temp[2*j+1] - 1 # 0,1,2,3,4,5,6,7 방향
        mat[i][j] = temp[2*j]
        fishes[temp[2*j]] = [i, j, d]
# 1. 첫번째 상어가 먹는다.
shark = [0, 0,  fishes[mat[0][0]][2], mat[0][0]]
fishes[mat[0][0]] = []
mat[0][0] = 20
score = 0
# 2. game을 시작한다.
game(0, 0, shark[2], shark[3], fishes, mat)
print(score)

