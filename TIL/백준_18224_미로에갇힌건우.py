def move(x,y, dx, dy):
    ox, oy = x, y
    while True:
        if not (0<= x< n and 0<= y < n):
            return ox, oy
        if mat[x][y] == 0:
            return x, y
        if mat[x][y] == -1:
            x,y = x+dx, y+dy
            continue
        if mat[x][y] > 0:
            return ox, oy
n, m = map(int, input().split())

mat = [[*map(lambda x:-int(x), input().split())] for _ in range(n)]

queue = [(0, 0, 1, 2)]
mat[0][0] = 1
near = ((0, -1), (0, 1), (1, 0), (-1, 0))
goal = False
count = 0
while queue:
    x, y, cnt, time = queue.pop(0)


    if x == n-1 and y == n-1:
        goal = True
        break

    for di, dj in near:
        temp = time
        newX, newY = x+di, y+dj
        if not (0 <= newX < n and 0 <= newY < n):
            continue
        if time == 3: # 밤
            if mat[newX][newY] == -1:
                newX, newY = move(newX, newY, di, dj)

        if not mat[newX][newY]:

            if cnt % m == 0:
                temp = time^1
            mat[newX][newY] = cnt+1
            queue.append((newX, newY, cnt+1, temp))

for a in mat:
    print(a)

if goal:
    if time == 2:

        print(((cnt-1)//(2*m))+1, 'sun')
    else:
        print(((cnt-1) // (2 * m)) + 1, 'moon')
else:
    print(-1)







