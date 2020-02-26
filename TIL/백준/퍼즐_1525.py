'''
make a hash
'''
from collections import deque
mat = [[*map(int, input().split())] for _ in range(3)]


def unboxing(num):
    temp = [[0] * 3 for _ in range(3)]
    for ii in range(3):
        for jj in range(3):
            temp[ii][jj] = num % 10
            num = num // 10
    return temp


def boxing(box, check):
    kkk = 0
    cnt = 0
    for i in range(3):
        for j in range(3):
            if check and box[i][j] == 0:
                syy, sxx = i, j
            kkk += (10 ** cnt) * box[i][j]
            cnt += 1
    if check:
        return syy, sxx, kkk
    else:
        return kkk


goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
goal_num = boxing(goal, False)
sy, sx, k = boxing(mat, True)
visited = dict()
visited[k] = 1
q = deque([(sy, sx, 0, k)])

near = ((1, 0), (0, 1), (-1, 0), (0, -1))
flag = -1
while q:
    y, x, res, kk = q.popleft()
    dummy = unboxing(kk)
    if kk == goal_num:
        flag = res
        break
    for dy, dx, in near:
        yy, xx = y+dy, x+dx
        if not (0 <= yy < 3 and 0 <= xx < 3):
            continue
        dummy[yy][xx], dummy[y][x] = dummy[y][x], dummy[yy][xx]
        k = boxing(dummy, False)
        if visited.get(k) is None:
            visited[k] = 1
            q.append((yy, xx, res+1, k))
        dummy[yy][xx], dummy[y][x] = dummy[y][x], dummy[yy][xx]

print(flag)
