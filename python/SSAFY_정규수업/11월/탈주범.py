from collections import deque
T = int(input())
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]



def tunnel(num):
    if num == 1:
        return (0, 1, 2,3)
    elif num == 2:
        return (0, 1)
    elif num == 3:
        return (2, 3)
    elif num == 4:
        return (0, 3)
    elif num == 5:
        return (1, 3)
    elif num == 6:
        return (1, 2)
    elif num == 7:
        return (0,2)


def bfs(x, y, l):
    q = [(x, y, 1)]
    cnt = 1
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    while q:
        x, y, time = q.pop(0)
        if l == time:
            break
        for k in range(4):
            if k in tunnel(mat[x][y]):
                xx , yy = x+di[k], y+dj[k]
                # x에서 xx로 갈 때, 맞다면 가고 아니면 말고
                if 0<= xx< n and 0<= yy< m and visited[xx][yy] == 0 and mat[xx][yy] != 0 and ( k^1 in tunnel(mat[xx][yy])):
                    q.append((xx, yy, time+1))
                    visited[xx][yy] = 1
                    cnt += 1
    return cnt



for t in range(1, T+1):
    #     맨홀x, y, 총 소요 시간
    n, m, r, c, l = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    print('#%s %s' % (t, bfs(r, c, l)))