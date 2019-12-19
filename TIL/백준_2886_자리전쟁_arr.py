n, m = map(int, input().strip().split())

mat = [list(input()) for _ in range(n)]
DEBUG = False
chair = []
people = []
short_cut = [{} for _ in range(n**2+m**2)]
for i in range(n):
    for j in range(m):

        if mat[i][j] == 'X':
            people.append((i, j))
        if mat[i][j] == 'L':
            chair.append((i, j))

cnt = 0


visited = [[0] * m for _ in range(n)]

for x, y in people:
    for i, j in chair:
        dis = (x-i) ** 2 + (y-j) ** 2
        if short_cut[dis].get((i,j)) == None:
            short_cut[dis][(i,j)] = [(x, y)]
        else:
            short_cut[dis][(i,j)].append((x,y))

if DEBUG:
    print(short_cut)

    for a in visited:
        print(a)
    print(len(short_cut))

for dic in short_cut:
    if len(dic):
        for key, values in dic.items():
            if visited[key[0]][key[1]]:
                continue
            flag = False
            for xx, yy in values:
                if visited[xx][yy]:
                    flag = True
                    break
            if flag:
                continue
            for xx, yy in values:
                visited[xx][yy] = 1
            if len(values) >= 2:
                cnt += 1
            visited[key[0]][key[1]] = 1
print(cnt)
