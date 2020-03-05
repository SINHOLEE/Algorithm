from collections import deque

n, m = map(int, input().split())

mat = [input() for _ in range(n)]

goals = {}
cnt1 = 0
for i in range(n):
    for j in range(m):
        if mat[i][j] == 'S':
            start = (i, j)
        if mat[i][j] == 'C':
            goals[(i,j)] = cnt1
            cnt1 += 1
queue = deque([(start[0], start[1], 0, 0, 0), (start[0], start[1], 1, 0, 0), (start[0], start[1], 2, 0, 0), (start[0], start[1], 3, 0, 0)])
visited = [[[[0]*4 for _ in range(4)] for _ in range(m)] for _ in range(n)]
for i in range(4):
    visited[start[0]][start[1]][0][i] = 1
        #상      하       우       좌
near = ((-1, 0), (1, 0), (0, 1), (0, -1))
# visited[x][y][key][d]
flag = False
while queue:
    x, y, d, cnt, key = queue.popleft()

    if key == 3:
        flag = True
        break

    for k in range(4):
        temp = key
        if k == d: # 같은 방향을 두 번 갈 수 없다.
            continue
        newX, newY = x+near[k][0], y+near[k][1]
        if not (0 <= newY < m and 0 <= newX < n):
            continue
        if mat[newX][newY] == '#':
            continue
        if visited[newX][newY][key][k]:
            continue
        if mat[newX][newY] == 'C':
            if key & 1 << goals[(newX, newY)] == 0:
                key = key | 1 << goals[(newX, newY)]
            else:
                continue
        visited[newX][newY][key][k] = 1
        queue.append((newX, newY, k, cnt+1, key))
        key = temp

if flag:
    print(cnt)
else:
    print(-1)