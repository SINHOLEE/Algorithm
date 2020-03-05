# 회전 버전

dx = [1, 0, -1, 0] # x
dy = [0, -1, 0, 1]
n = int(input())
mat = [[0] * 101 for _ in range(101)]

for _ in range(n):
    sx, sy, d, generation = map(int, input().split())
    my_lis = [d]
    mat[sy][sx] = 1
    sx += dx[d]
    sy += dy[d]
    mat[sy][sx] = 1
    for _ in range(generation):
        new = [(i+1)%4 for i in my_lis[::-1]]
        for dd in new:
            sx += dx[dd]
            sy += dy[dd]
            mat[sy][sx] = 1
        my_lis += new
cnt = 0
for i in range(100):
    for j in range(100):
        if mat[i][j] and mat[i+1][j] and mat[i][j+1] and mat[i+1][j+1]:
            cnt += 1

print(cnt)

'''
# 내코드
dj = [1, 0, -1, 0] # x
di = [0, -1, 0, 1]
n = int(input())
mat = [[0] * 101 for _ in range(101)]

for _ in range(n):
    sx, sy, d, generation = map(int, input().split())
    my_lis = [(sx, sy), (sx+dj[d], sy+di[d])]
    mat[sy][sx] = 1
    mat[sy+di[d]][sx+dj[d]] = 1
    for _ in range(generation):
        ox, oy = my_lis[-1]
        for i in range(len(my_lis)-1, -1, -1):
            if i == len(my_lis)-1:
                continue
            dx = my_lis[i][0] - ox
            dy = my_lis[i][1] - oy
            mat[oy+dx][ox-dy] = 1
            my_lis.append((ox - dy, oy + dx))

cnt = 0
for i in range(100):
    for j in range(100):
        if mat[i][j] and mat[i+1][j] and mat[i][j+1] and mat[i+1][j+1]:
            cnt += 1

print(cnt)

'''