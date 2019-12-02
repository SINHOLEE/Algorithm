n,m=map(int,input().split())

mat = [input(str()) for _ in range(n)]
   # 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
DEBUG=False
def bfs(rrx,rry,bbx,bby):
    visited = [[[[0] * 10 for _ in range(10)] for _ in range(10)] for _ in range(10)]
    visited[rrx][rry][bbx][bby] = 1
    q = [(rrx,rry,bbx,bby,0, 0)]
    while q:
        rrx, rry, bbx, bby, d, cnt = q.pop(0)
        if cnt >= 10:
            cnt = -1
            return cnt
        for k in range(4):
            rx,ry,bx,by = rrx,rry,bbx,bby
            if (k == d or k == d^1) and cnt!=0:
                continue
            r_goal = False
            r_cnt = 0
            while True:
                new_rx, new_ry = rx+di[k], ry+dj[k]
                if mat[new_rx][new_ry] == '#':
                    break
                if mat[new_rx][new_ry] == 'O':
                    r_goal = True
                    break
                r_cnt += 1
                rx, ry = new_rx, new_ry
            b_goal = False
            b_cnt = 0
            while True:
                new_bx, new_by = bx + di[k], by + dj[k]
                if mat[new_bx][new_by] == '#':
                    break
                if mat[new_bx][new_by] == 'O':
                    b_goal = True
                    break
                b_cnt += 1
                bx, by = new_bx, new_by
            if rx==bx and ry==by:
                if r_cnt > b_cnt:
                    rx -= di[k]
                    ry -= dj[k]
                else:
                    bx -= di[k]
                    by -= dj[k]
            if b_goal:
                continue
            if r_goal == True:
                cnt+=1
                return cnt

            if visited[rx][ry][bx][by] == 0:
                visited[rx][ry][bx][by] = 1
                q.append((rx,ry,bx,by,k,cnt+1))
                if DEBUG:
                    print('visited', visited)
                    print('red',rx,ry)
                    print('blue', bx,by)
                    print('cnt', cnt, 'r-goal', r_goal, 'b_goal',b_goal)
                    print('direction', d)
                    print('k',k)
                    print()
    cnt = -1
    return cnt

for i in range(n):
    for j in range(m):
        if mat[i][j] == 'R':
            red = (i,j)
            mat[i] = mat[i].replace('R','.')
        if mat[i][j] == 'B':
            blue = (i, j)
            mat[i] = mat[i].replace('B','.')

print(bfs(red[0], red[1], blue[0], blue[1]))