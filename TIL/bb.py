def move(y, x, cnt):
    global res, n, flag
    if flag:
        return
    if y == n-1 and x == n-1 and cnt == 2*n-2:
        flag = True
        print("Case #%s: %s" %(t, ''.join(res)))
        return
    for d in ( "E", "S"):
        ny, nx = y+dy[d], x+dx[d]
        if not (0<=ny<n and 0<=nx<n):
            continue
        if mat[ny][nx][dx[d]]:
            continue
        res.append(d)
        move(ny, nx, cnt+1)
        res.pop()




    # e  s
dy = {
    "S": 1,
    "E": 0
}
dx = {
    "S": 0,
    "E": 1
}

for t in range(1, int(input())+1):
    n = int(input())
    mat = [[[0, 0] for _ in range(n)] for _ in range(n)]
    route = input()

    x = 0
    y = 0
    res = []
    for d in route:
        y, x = y + dy[d], x+dx[d]
        mat[y][x][dx[d]] = 1

    flag = False
    move(0, 0, 0)

