'''
갯수세기 조건을 간과하지 말자
'''

near = ((0,1),(0,-1),(1,0),(-1,0))

def bfs(lis):
    global total_zero
    temp_zero = total_zero
    this_mat = [arr[:] for arr in mat]
    q = []
    for idx in lis:
        x, y = virus[idx][0], virus[idx][1]
        this_mat[x][y] = 2501
        q.append((x, y))
    cnt = 0
    while q:
        if temp_zero <= 0:
            break
        for _ in range(len(q)):
            x, y = q.pop(0)

            for di, dj in near:
                newX, newY = x + di, y + dj
                if not (0 <= newX < n and 0 <= newY < n):
                    continue
                if this_mat[newX][newY] == -2:
                    this_mat[newX][newY] = 2501
                    q.append((newX, newY))

                if this_mat[newX][newY] == 0:
                    this_mat[newX][newY] = cnt + 1
                    q.append((newX, newY))
                    temp_zero -= 1
        cnt += 1



    for i in range(n):
        for j in range(n):
            if this_mat[i][j] == 0:
                return 987654321
    else:
        return cnt


def combi(target, depth, lis):
    global min_value
    if depth == m:
        min_value = min(min_value, bfs(lis))
        return

    for i in range(target, len(virus)):
        if visited[i] == 0:
            visited[i] = 1
            combi(i, depth+1, lis + [i])
            visited[i] = 0
n, m = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]
virus = []
total_zero = n ** 2
for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            mat[i][j] = -1
            total_zero -=1
        if mat[i][j] == 2:
            mat[i][j] = -2
            virus.append((i, j))
            total_zero -= 1
min_value = 987654321
visited = [0] * len(virus)
combi(0, 0, [])
if min_value == 987654321:
    print(-1)
else:
    print(min_value)

