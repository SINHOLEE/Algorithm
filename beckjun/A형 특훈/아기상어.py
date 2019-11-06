from pprint import pprint
n = int(input())

mat = [list(map(int, input().split())) for _ in range(n)]
visited_dummy = [[False] * n for _ in range(n)]

locations = [{} for _ in range(7)]

for i in range(n):
    for j in range(n):
        if mat[i][j]:
            if mat[i][j] == 9:
                shark = [i, j, 2, 0]
            else:
                locations[mat[i][j]][(i,j)] = mat[i][j]
    # 좌 우 상 하
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def find(x, y, goal_x, goal_y, res):
    global temp_dis
    if temp_dis < res:
        return
    if x == goal_x and y == goal_y:
        if temp_dis > res:
            temp_dis = res

        return

    for k in range(4):
        if x+di[k] >= 0 and x+di[k] < n and y+dj[k] >= 0 and y+dj[k] < n and visited[x+di[k]][y+dj[k]] == False:
            visited[x+di[k]][y+dj[k]] = True
            find(x+di[k], y+dj[k], goal_x, goal_y, res+1)
            visited[x + di[k]][y + dj[k]] = False

total = 0

visited = [arr[:] for arr in visited_dummy]
while True:
    #
    now_data = []
    for i in range(1, 7):
        if i < shark[2]:
            temp_dis = 999999999
            for key, val in locations[i].items():
                x, y = key[0], key[1]
                visited[x][y] = True
                find(x, y, shark[0], shark[1], 0)
                visited[x][y] = False
                if len(now_data) == 0:
                    if temp_dis == 999999999:
                        pass
                    elif temp_dis < 999999999:
                        now_data = [temp_dis, x, y]
                else:
                    if now_data[0] > temp_dis:
                        now_data[0] = temp_dis
                        now_data[1] = x
                        now_data[2] = y
    if len(now_data) == 0:
        break
    else:
        distance = now_data[0]
        xx = now_data[1]
        yy = now_data[2]
        total += distance
        shark[0] = xx
        shark[1] = yy
        shark[3] += 1
        if shark[3] == shark[2]:
            shark[3] = 0
            shark[2] += 1
        del(locations[mat[xx][yy]][(xx, yy)])
        mat[xx][yy] = 0
print(total)
