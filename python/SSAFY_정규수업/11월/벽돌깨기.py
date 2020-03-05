from collections import deque

di = [0,0,1,-1]
dj = [-1,1,0,0]

DEBUG = False
def bfs(x, y, mat):
    cnt = 1
    t, tt = x, y
    visited = [[0] * w for _ in range(h)]
    visited[x][y] = 1
    q = deque([(x, y , mat[x][y])])
    mat[x][y] = 0
    # 폭발 퍼지는 로직
    while q:
        x, y, length = q.popleft()
        for power in range(length):
            for k in range(4):
                xx, yy = x + ( di[k] * power), y + ( dj[k] * power )
                if 0<= xx< h and 0<= yy<w and visited[xx][yy] == 0 and mat[xx][yy] != 0:
                    q.append((xx, yy, mat[xx][yy]))
                    mat[xx][yy] = 0
                    visited[xx][yy] = 1
                    cnt += 1

    if DEBUG:
        print(t, tt)
        for a in visited:
            print(a)
        print('삭제전')
        for b in mat:
            print(b)

    # 폭발 후  로직
    for j in range(w):
        for i in range(h-1, -1,-1): # 열 기준, 좌에서 우로, 행기준 아래서 위로 이동
            if mat[i][j]:
                continue
            for k in range(i, -1,-1):
                x, y = k, j
                while True:
                    if not 0 <= x < h:
                        flag = True
                        break
                    if mat[x][y] != 0:
                        while True:
                            xx = x + 1
                            if not (0 <= xx < h):
                                break
                            if mat[xx][y] != 0:
                                visited[xx][y] = 2
                                break
                            if visited[xx][y] == 2:
                                break
                            mat[xx][y], mat[x][y] = mat[x][y], mat[xx][y]
                            x = xx
                        break
                    x -= 1


    if DEBUG:
        print('삭제후')
        for c in mat:
            print(c)
        print(cnt)
    return cnt, mat



def drop(idx_of_w, mat):
    cnt = 0
    for _ in range(h):
        if mat[_][idx_of_w] != 0:
            cnt, mat = bfs(_, idx_of_w,mat)
            break
    return cnt, mat

def perm(depth, lis):
    global total_block, min_val, mat_dummy
    if min_val == 0:
        return
    if depth == n:
        mat = [arr[:] for arr in mat_dummy]
        cnt_break = 0
        for idx in lis:
            cnt, mat = drop(idx, mat)
            cnt_break += cnt

        if min_val > total_block - cnt_break:
            min_val = total_block - cnt_break

        return

    for i in range(w):
        perm(depth+1, lis + [i])

T = int(input())
for t in range(1, T+1):
    n, w, h = map(int, input().split())
    mat_dummy = [list(map(int, input().split())) for _ in range(h)]
    total_block = w*h - sum(mat_dummy,[]).count(0)


    min_val = 987654321
    perm(0,[])
    print('#%s %s' % (t, min_val))