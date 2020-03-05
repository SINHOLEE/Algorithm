from collections import deque
near = [[-1,0], [0,1], [1,0], [0,-1]]
def go():
    global rs
    q = deque()
    x,y = ht[0]
    gx1, gy1 = ht[1]
    gx2, gy2 = ht[2]
    for i in range(4):
        a,b = near[i]
        xi, yi = a+x, b+y
        if 0 <= xi < n and 0 <= yi < m:
            q.append([xi,yi,i,0,0])
            vis[xi][yi][i][0][0] = 1
    time = 0
    while q:
        for i in range(len(q)):
            x,y,d,g1,g2 = q.popleft()
            if g1 + g2 == 2:
                rs = time
                return
            for j in range(4):
                if j != d:
                    t1, t2 = g1, g2
                    a,b = near[j]
                    xi, yi = a+x, b+y
                    if 0 <= xi < n and 0 <= yi < m and bd[xi][yi] == '.' and vis[xi][yi][j][g1][g2] == 0:
                        flag1, flag2 = False, False
                        if xi == gx1 and yi == gy1:
                            if g1:
                                flag1 = True
                                continue
                            else:
                                g1 = 1
                        elif xi == gx2 and yi == gy2:
                            if g2:
                                flag2 = True
                                continue
                            else:
                                g2 = 1

                        q.append([xi,yi,j,g1,g2])
                        vis[xi][yi][j][g1][g2] = 1
                        g1,g2 = t1, t2
        time += 1
n,m = map(int,input().split())
bd = [list(input()) for i in range(n)]
vis = [[[[[0]*2 for i in range(2)] for i in range(4)] for i in range(m)] for i in range(n)]
gift = 1
ht = {}
for x in range(n):
    for y in range(m):
        if bd[x][y] == 'S':
            ht[0] = (x,y)
            bd[x][y] = '.'
        elif bd[x][y] == 'C':
            ht[gift] = (x,y)
            bd[x][y] = '.'
            gift += 1
rs = -1
go()
print(rs)

