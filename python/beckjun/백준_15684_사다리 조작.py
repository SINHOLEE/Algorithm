dx = [1, -1, 0]
dy = [0, 0, 1]

c = 0
def combi(idx, depth):
    global min_value,c
    c+=1
    if min_value <= depth:
        return

    if check([arr[:] for arr in matrix]):
        min_value = min(depth, min_value)
        # 하루종일 너때문에....
        return


    if depth >= 3:
        return

    for j in range(idx,len(combi_list)):
        if combi_visited[j]:
            continue
        x, y = combi_list[j][1], combi_list[j][0]
        if 0<= x-2 and matrix[y][x-2]:
            continue
        if x+2<n*2+1 and matrix[y][x+2]:
            continue
        combi_visited[j] = 1
        matrix[y][x] = 1
        combi(j, depth+1)
        combi_visited[j] = 0
        matrix[y][x] = 0


def check(mat):
    for xx in range(2, n*2+1, 2):
        x = xx
        for y in range(h + 2):
            # 맨 왼쪽
            if x == n * 2:
                if mat[y][x - 1]:
                    x = x - 2
            else:
                if mat[y][x - 1]:
                    x = x - 2
                else:
                    if mat[y][x + 1]:
                        x = x + 2
        if x != xx:
            return False
    else:
        return True


n, m, h = map(int, input().split())

matrix = [[0] * (n*2+1) for _ in range(h+2)]
for i in range(h+2):
    for j in range(2, n*2+1, 2):
        matrix[i][j] = 1

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b*2+1] = 1


combi_list = []
for i in range(1,h+1):
    for j in range(3, n * 2 +1, 2):
        if matrix[i][j]:
            continue
        combi_list.append((i, j))

combi_visited = [0] * len(combi_list)

min_value = 4
combi(0, 0)
if min_value == 4:
    print(-1)
else:
    print(min_value)
print(c)