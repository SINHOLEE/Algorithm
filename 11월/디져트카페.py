di = [1, 1, -1,-1]
dj = [1, -1, -1, 1]
def move(x, y, lis, k):
    global s_x, s_y, max_visited
    print('s',s_x, s_y)
    print(x, y)
    print(lis)
    print()
    if s_x == x and s_y == y:
        if max_visited < len(lis):
            max_visited = len(lis)
        return
    xx, yy = x+di[k], y + dj[k]
    if 0<= xx<n and 0<=yy<n:
        if mat[xx][yy] not in lis:
            move(xx,yy,lis+[mat[xx][yy]], k)
            if k < 3:
                xx, yy = x+di[k+1], y+dj[k+1]
                if mat[xx][yy] not in lis:
                    move(xx, yy, lis+[mat[xx][yy]], k+1)



T = int(input())

for t in range(1, T+1):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    max_visited = 0
    for i in range(n-2):
        for j in range(1,n-1):
            s_x, s_y = i, j
            move(i+1, j+1, [mat[i+1][j+1]], 0)
    if max_visited == 0:
        print(-1)
    else:
        print(max_visited)
