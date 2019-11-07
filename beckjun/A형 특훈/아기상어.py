'''
bfs 제대로 쓰자...

'''

n = int(input())

mat = [list(map(int, input().split())) for _ in range(n)]
    # 좌 우 상 하
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

fish_cnt = 0
for i in range(n):
    for j in range(n):
        if mat[i][j]:
            if mat[i][j] == 9:
                mat[i][j] = 0
                shark = [i, j, 2, 0]
            else:
                fish_cnt += 1

total_time = 0
flag = True
while True:
    if fish_cnt == 0 or flag == False:
        break
    queue = [(shark[0], shark[1])]
    time = 0
    visited_dummy = [[False] * n for _ in range(n)]
    visited_dummy[shark[0]][shark[1]] = True
    while True:
        flag = False
        if len(queue) == 0:
            break
        queue.sort()
        for q in range(len(queue)):
            x, y = queue.pop(0)
            if mat[x][y] != 0 and mat[x][y] < shark[2]:
                flag = True
                break

            for k in range(4):
                if x+di[k] >= 0 and  x+di[k] < n and y+dj[k] >= 0 and y+dj[k] < n and visited_dummy[x+di[k]][y+dj[k]] == False and mat[x+di[k]][y+dj[k]] <= shark[2]:
                    queue.append((x+di[k], y+dj[k]))
                    visited_dummy[x+di[k]][y+dj[k]] = True



        # 먹었으면 어떻게 되는지
        if flag:
            fish_cnt -= 1
            mat[x][y] = 0
            shark[0] = x
            shark[1] = y
            shark[3] += 1
            if shark[3] == shark[2]:
                shark[2] += 1
                shark[3] = 0
            total_time += time
            break
        else:
            time+=1

print(total_time)


