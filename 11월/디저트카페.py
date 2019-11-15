di = [1, 1, -1,-1]
dj = [1, -1, -1, 1]
def move(x, y, lis, k):
    global s_x, s_y, max_visited
    if s_x == x and s_y == y:
        if max_visited < len(lis):
            max_visited = len(lis)
        return
    if s_x+s_y == x+y and k == 2: # 스타트지점에서 좌하향 라인과 같다면 2번방향(좌상)으로 가는것을 멈추고 우상으로 간다.
        xx, yy = x + di[3], y + dj[3]
        if 0 <= xx < n and 0 <= yy < n:
            if mat[xx][yy] not in lis:
                move(xx, yy, lis + [mat[xx][yy]], k)
    else:
        xx, yy = x+di[k], y + dj[k]
        if 0<= xx<n and 0<=yy<n:
            if mat[xx][yy] not in lis:
                move(xx,yy,lis+[mat[xx][yy]], k)
        if k < 2:
            xx, yy = x+di[k+1], y+dj[k+1]
            if 0 <= xx < n and 0 <= yy < n:
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
        print('#%s %s' % (t, -1))
    else:
        print('#%s %s'% (t, max_visited))
