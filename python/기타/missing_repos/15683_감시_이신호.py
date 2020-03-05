di = [-1,0,1,0]
dj = [0,1,0,-1]

def dfs(depth, board, zero_cnt):
    global min_val,cnt
    cnt+=1
    if DEBUG:
        print()
        print(cnt)
        print('depth',depth)
        print(min_val)
        for a in board:
            print(a)

    if len(cctv) == depth:
        if min_val > zero_cnt:
            min_val = zero_cnt
        return

    cctvX, cctvY = cctv[depth][0], cctv[depth][1]
    for k in range(4):
        board_copy, zero_cnt_temp = cctv_ty(cctvX, cctvY, [arr[:] for arr in board], k, board[cctvX][cctvY], zero_cnt)

        dfs(depth+1, board_copy, zero_cnt_temp)


def cctv_ty(x,y,board, d, ty, zero_cnt):
    if ty == 1:
        return fillup(x,y,board,d, zero_cnt)
    elif ty == 2:
        board, zero_cnt_temp = fillup(x, y, board, d, zero_cnt)
        board, zero_cnt_temp = fillup(x, y, board, (d + 2) % 4, zero_cnt_temp)
        return board, zero_cnt_temp
    elif ty == 3:
        board, zero_cnt_temp = fillup(x, y, board, d,zero_cnt)
        board, zero_cnt_temp = fillup(x, y, board, (d + 1) % 4, zero_cnt_temp)
        return board, zero_cnt_temp
    else:
        board,zero_cnt_temp = fillup(x, y, board, d,zero_cnt)
        board, zero_cnt_temp = fillup(x, y, board, (d + 1) % 4, zero_cnt_temp)
        board, zero_cnt_temp = fillup(x, y, board, (d + 2) % 4, zero_cnt_temp)
        return board, zero_cnt_temp


def fillup(x,y,board,d, zero_cnt):
    while True:
        newX, newY = x+di[d], y+dj[d]
        if not (0<= newX<n and 0<= newY<m):
            break
        if board[newX][newY] == 6:
            break
        if 1<= board[newX][newY] <= 5 or board[newX][newY] == -1:
            x, y = newX, newY
            continue
        board[newX][newY] = -1
        zero_cnt-=1
        x,y = newX,newY
    return board, zero_cnt

n,m = map(int, input().split())

mat = [[*map(int, input().split())] for _ in range(n)]
DEBUG = False
DEBUG2 = False

cctv = []
min_val = 0
for i in range(n):
    for j in range(m):
        if 1<= mat[i][j]<5:
            cctv.append((i,j))
        elif mat[i][j] == 5:
            for k in range(4):
                mat, nono = fillup(i,j,mat,k,0)
for i in range(n):
    for j in range(m):
        if mat[i][j] == 0:
            min_val+=1
zero_cnt = min_val
if DEBUG2:
    print('start')
    for arr in mat:
        print(arr)
    print(cctv)
cnt = 0
#
visited = [0] * len(cctv)

dfs(0, [arr[:] for arr in mat], zero_cnt)
print(min_val)