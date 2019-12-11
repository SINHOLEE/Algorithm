            #우 좌 상 하
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def white(i, j, d):
    current = mat[i][j]
    mat[i + di[d]][j + dj[d]] +=  current
    mat[i][j] = []
    for v in mat[i + di[d]][j + dj[d]]:
        new_i = i+di[d]
        new_j = j+dj[d]
        new_d = locations[v][2]
        locations[v] = (new_i, new_j, new_d)
    return len(mat[i + di[d]][j + dj[d]])

def red(i, j, d):
    current = mat[i][j]
    mat[i + di[d]][j + dj[d]] +=  current[::-1]
    mat[i][j] = []
    for v in mat[i + di[d]][j + dj[d]]:
        new_i = i+di[d]
        new_j = j+dj[d]
        new_d = locations[v][2]
        locations[v] = (new_i, new_j, new_d)
    return len(mat[i + di[d]][j + dj[d]])


n, k = map(int, input().split())

color_board = [list(map(int, input().split())) for i in range(n)]

mat = [[[] for _ in range(n)] for _ in range(n)]
locations = []

for h in range(k): # h는 순서를 정하기 위한 장치 0 ~ k-1 번
    i, j, d = map(int, input().split())
    locations.append((i-1, j-1, d-1))
    mat[i-1][j-1].append(h)

count = 0
flag = False
while True:
    total = 0  # 매번 for 문을 돌 때 마다 세는 것... 각 말이 이동한 뒤 업혀있는 말들의 총 개수
    for h in range(k):
        if mat[locations[h][0]][locations[h][1]][0] == h:
            i = locations[h][0]
            j = locations[h][1]
            d = locations[h][2]
            if (i + di[d] < 0 or i + di[d] > n-1 or j + dj[d] < 0 or j + dj[d] > n-1) or color_board[i+di[d]][j+dj[d]] == 2: # 갈곳이 파랑색이거나 벽이라면,
                d ^= 1
                locations[h] = (i, j, d)
                if (i + di[d] < 0 or i + di[d] > n - 1 or j + dj[d] < 0 or j + dj[d] > n - 1) or color_board[i + di[d]][j + dj[d]] == 2:  # 갈곳이 파랑색이거나 벽이라면,
                    total = len(mat[i][j])
                elif color_board[i + di[d]][j + dj[d]] == 0:  # 갈 곳이 하양이라면,
                    total = white(i, j, d)
                elif color_board[i + di[d]][j + dj[d]] == 1:
                    total = red(i, j, d)
            elif color_board[i+di[d]][j+dj[d]] == 0:
                total = white(i, j, d)
            elif color_board[i+di[d]][j+dj[d]] == 1:
                total = red(i, j, d)
        if total >= 4 or count >= 1000:
            flag = True
            break
    count += 1

    if flag:
        break

if count > 1000:
    print('-1')
else:
    print(count)
