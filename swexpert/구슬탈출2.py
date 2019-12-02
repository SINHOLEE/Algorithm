from collections import deque

def bfs(rx,ry, bx,by):
    global min_cnt
              # rx, ry, bx, by, cnt
    q = deque([[rx,ry,bx, by, 0]])
    while True:
        if len(q) == 0:
            min_cnt = -1
            break
        rx,ry,bx, by,cnt = q.popleft()
        r = (rx,ry)
        b= (bx,by)
        if cnt == 10:
            min_cnt = -1
            break
        flag = False
        for k in range(4):
            if k == 0: # 오른쪽
                temp = move_right(cnt,r, b)
                if temp == 0:  # b_goal일때
                    continue
                if len(temp) == 1:
                    flag = True
                    min_cnt = temp[0]
                    break
                else:
                    q.append((temp[0], temp[1][0], temp[1][1], temp[2][0],temp[2][1])) # 다음 단계로 진행
            elif k == 1: # 왼쪽
                temp = move_left(cnt,r, b)
                if temp == 0:  # b_goal일때
                    continue
                if len(temp) == 1:
                    flag = True
                    min_cnt = temp[0]
                    break
                else:
                    q.append((temp[0], temp[1][0], temp[1][1], temp[2][0],temp[2][1])) # 다음 단계로 진행
            elif k == 2:
                temp = move_up(cnt,r, b)
                if temp == 0:  # b_goal일때
                    continue
                if len(temp) == 1:
                    flag = True
                    min_cnt = temp[0]
                    break
                else:
                    q.append((temp[0], temp[1][0], temp[1][1], temp[2][0],temp[2][1])) # 다음 단계로 진행
            else:
                temp = move_down(cnt,r, b)
                if temp == 0:  # b_goal일때
                    continue
                if len(temp) == 1:
                    flag = True
                    min_cnt = temp[0]
                    break
                else:
                    q.append((temp[0], temp[1][0], temp[1][1], temp[2][0],temp[2][1])) # 다음 단계로 진행

        if flag:
            break



n, m = map(int, input().split())

mat1 = [ str(input()) for _ in range(n)]

def move_right(cnt, r, b):
    new_rx, new_ry = r[0], r[1]
    new_bx, new_by = b[0], b[1]
    b_goal = False
    is_passed = False
    while True: # 오른쪽으로 움직인다.
        next_bx, next_by = new_bx, new_by + 1

        if next_bx == r[0] and next_by == r[1]:
            is_passed = True
        if mat[next_bx][next_by] == 0:
            new_bx,new_by = next_bx,next_by
        elif mat[next_bx][next_by] == 9:
            b_goal = True
            break
        elif mat[next_bx][next_by] == 1:
            break

    if b_goal:
        return 0

    r_goal = False
    while True:
        next_rx, next_ry = new_rx, new_ry + 1
        if mat[next_rx][next_ry] == 0:
            new_rx,new_ry = next_rx,next_ry
        elif mat[next_rx][next_ry] == 9:
            r_goal = True
            break
        elif mat[next_rx][next_ry] == 1:
            break
    if r_goal:
        return [cnt+1]

    if
    if is_passed == False:
        return (cnt+1,(new_rx,new_ry), (new_bx,new_by))
    else:
        return (cnt+1,(new_rx,new_ry), (new_bx, new_by-1))

def move_left(cnt, r, b):
    new_rx, new_ry = r[0], r[1]
    new_bx, new_by = b[0], b[1]
    b_goal = False
    is_passed = False
    while True: # 오른쪽으로 움직인다.
        next_bx, next_by = new_bx, new_by - 1

        if next_bx == r[0] and next_by == r[1]:
            is_passed = True
        if mat[next_bx][next_by] == 0:
            new_bx,new_by = next_bx,next_by
        elif mat[next_bx][next_by] == 9:
            b_goal = True
            break
        elif mat[next_bx][next_by] == 1:
            break

    if b_goal:
        return 0

    r_goal = False
    while True:
        next_rx, next_ry = new_rx, new_ry - 1
        if mat[next_rx][next_ry] == 0:
            new_rx,new_ry = next_rx,next_ry
        elif mat[next_rx][next_ry] == 9:
            r_goal = True
            break
        elif mat[next_rx][next_ry] == 1:
            break
    if r_goal:
        return [cnt+1]
    if new_bx == b[0] and new_by == b[1] and new_rx ==r[0] and new_ry == r[1]:
        return 0
    if is_passed == False:
        return (cnt+1,(new_rx,new_ry), (new_bx,new_by))
    else:
        return (cnt+1,(new_rx,new_ry), (new_bx, new_by+1))

def move_up(cnt, r, b):
    new_rx, new_ry = r[0], r[1]
    new_bx, new_by = b[0], b[1]
    b_goal = False
    is_passed = False
    while True: # 오른쪽으로 움직인다.
        next_bx, next_by = new_bx-1, new_by

        if next_bx == r[0] and next_by == r[1]:
            is_passed = True
        if mat[next_bx][next_by] == 0:
            new_bx,new_by = next_bx,next_by
        elif mat[next_bx][next_by] == 9:
            b_goal = True
            break
        elif mat[next_bx][next_by] == 1:
            break

    if b_goal:
        return 0

    r_goal = False
    while True:
        next_rx, next_ry = new_rx-1, new_ry
        if mat[next_rx][next_ry] == 0:
            new_rx,new_ry = next_rx,next_ry
        elif mat[next_rx][next_ry] == 9:
            r_goal = True
            break
        elif mat[next_rx][next_ry] == 1:
            break
    if r_goal:
        return [cnt+1]
    if new_bx == b[0] and new_by == b[1] and new_rx ==r[0] and new_ry == r[1]:
        return 0
    if is_passed == False:
        return (cnt+1,(new_rx,new_ry), (new_bx,new_by))
    else:
        return (cnt+1,(new_rx,new_ry), (new_bx+1, new_by))

def move_down(cnt, r, b):
    new_rx, new_ry = r[0], r[1]
    new_bx, new_by = b[0], b[1]
    b_goal = False
    is_passed = False
    while True: # 오른쪽으로 움직인다.
        next_bx, next_by = new_bx+1, new_by

        if next_bx == r[0] and next_by == r[1]:
            is_passed = True
        if mat[next_bx][next_by] == 0:
            new_bx,new_by = next_bx,next_by
        elif mat[next_bx][next_by] == 9:
            b_goal = True
            break
        elif mat[next_bx][next_by] == 1:
            break

    if b_goal:
        return 0

    r_goal = False
    while True:
        next_rx, next_ry = new_rx+1, new_ry
        if mat[next_rx][next_ry] == 0:
            new_rx,new_ry = next_rx,next_ry
        elif mat[next_rx][next_ry] == 9:
            r_goal = True
            break
        elif mat[next_rx][next_ry] == 1:
            break
    if r_goal:
        return [cnt+1]
    if new_bx == b[0] and new_by == b[1] and new_rx ==r[0] and new_ry == r[1]:
        return 0
    if is_passed == False:
        return (cnt+1,(new_rx,new_ry), (new_bx,new_by))
    else:
        return (cnt+1,(new_rx,new_ry), (new_bx-1, new_by))

mat = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if mat1[i][j] == '#':
            mat[i][j] = 1
        if mat1[i][j] == 'R':
            red = [i, j]
        if mat1[i][j] == 'B':
            blue = [i, j]
        if mat1[i][j] == 'O':
            goal = (i, j)
            mat[i][j] = 9
bfs(red[0],red[1], blue[0],blue[1])
print(min_cnt)