from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

mat = [[*map(lambda x: -(int(x)), input().split())] for _ in range(n)]
flag = False
head = -1
tail = 0
dq = [None] * (n*m)
for i in range(n):
    for j in range(m):
        if mat[i][j] == -2:
            flag = True
            mat[i][j] = 0
            dq[0] = (i,j,0)
            break
    if flag:
        break
near = ((0, 1), (0, -1), (1, 0), (-1, 0))

while tail != head:
    head += 1
    x, y, cnt = dq[head]

    for di, dj in near:
        newX, newY = x + di, y + dj
        if not (0 <= newX < n and 0 <= newY < m):
            continue
        if mat[newX][newY] == -1:
            mat[newX][newY] = cnt+1
            tail += 1
            dq[tail] = (newX, newY, cnt + 1)


for a in mat:
    print(' '.join(map(str, a)))