def charger(ay,ax,by,bx):
    unit_max_charged = 0
    for first_idx in range(a):
        for second_idx in range(a):
            if first_idx == second_idx and mat[ay][ax][first_idx]>0 and mat[by][bx][second_idx]>0:
                unit_max_charged = max(mat[ay][ax][first_idx] // 2 + mat[by][bx][second_idx] // 2, unit_max_charged)
            else:
                unit_max_charged = max(mat[ay][ax][first_idx]+mat[by][bx][second_idx], unit_max_charged)
    return unit_max_charged
dy = (0,-1,0,1,0)
dx = (0,0,1,0,-1)

T = int(input())

for t in range(1, T+1):
    m, a = map(int, input().split())
    mat = [[[0] *a for _ in range(11)] for _ in range(11)]

    a_line = [*map(int, input().split())]
    b_line = [*map(int, input().split())]
    for times in range(a):
        visited = [[0]*11 for _ in range(11)]
        x, y, c, p = map(int, input().split())
        visited[y][x] = 1
        mat[y][x][times] = p
        q = [(y, x)]

        newc = 1
        while q:
            if c+1 == newc:
                break
            for _ in range(len(q)):
                yy, xx = q.pop(0)
                for k in range(1,5):
                    newY,newX = yy+dy[k], xx+dx[k]
                    if not (1<=newY<11 and 1<=newX<11):
                        continue
                    if visited[newY][newX]:
                        continue
                    q.append((newY, newX))
                    visited[newY][newX] = newc
                    mat[newY][newX][times] = p
            newc+=1


    # #
    men = [(1,1,10,10)]

    total_cg = charger(1,1, 10, 10)
    for qqqqq in range(m):
        ay, ax, by, bx = men.pop()
        neway, newax, newby, newbx = ay + dy[a_line[qqqqq]], ax + dx[a_line[qqqqq]], by + dy[b_line[qqqqq]], bx + dx[b_line[qqqqq]]
        men.append(( neway, newax, newby, newbx ))
        total_cg += charger( neway, newax, newby, newbx )
    print('#%s %s' % (t, total_cg))