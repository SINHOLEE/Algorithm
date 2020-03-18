import sys
from collections import deque
input = sys.stdin.readline

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)
for t in range(1, int(input())+1):
    m, n = map(int,input().split())
    mat = [list(input()) for _ in range(n)]

    res = "IMPOSSIBLE"

    fire = deque([])
    for i in range(n):
        for j in range(m):
            if mat[i][j] == "@":
                human = deque([(i, j)])
            if mat[i][j] == "*":
                fire.append((i, j))

    cnt = 0
    while human:

        if res != "IMPOSSIBLE":
            break
        for _ in range(len(human)):
            if res != "IMPOSSIBLE":
                break
            y, x = human.popleft()
            if mat[y][x] == "*":
                continue
            for k in range(4):
                yy, xx = y+dy[k], x+dx[k]
                if not (0 <= yy < n and 0 <= xx < m):
                    res = cnt + 1
                    break
                if mat[yy][xx] == "@":
                    continue
                if mat[yy][xx] == "*":
                    continue
                if mat[yy][xx] == "#":
                    continue
                if mat[yy][xx] == ".":
                    mat[yy][xx] = "@"
                    human.append((yy, xx))

        for __ in range(len(fire)):
            fy, fx = fire.popleft()
            for kk in range(4):
                fyy, fxx = fy+dy[kk], fx+dx[kk]
                if not (0 <= fyy < n and 0 <= fxx < m):
                    continue
                if mat[fyy][fxx] == "#":
                    continue
                if mat[fyy][fxx] == "*":
                    continue
                if mat[fyy][fxx] == "." or mat[fyy][fxx] == "@":
                    mat[fyy][fxx] = "*"
                    fire.append((fyy, fxx))
        cnt += 1

    print(res)
