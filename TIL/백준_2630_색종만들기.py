n = int(input())


def recursion(sx=0, sy=0, ex=n, ey=n):
    temp = mat[sx][sy]
    dummy = sum([mat[i][j] for i in range(sx, ex) for j in range(sy, ey)])
    if dummy == (ex-sx)**2 or dummy == 0:
        res[temp] += 1
    else:
        mx = (sx + ex) // 2
        my = (sy + ey) // 2
        recursion(sx, sy, mx, my)
        recursion(mx, sy, ex, my)
        recursion(sx, my, mx, ey)
        recursion(mx, my, ex, ey)


mat = [[*map(int, input().split())] for _ in range(n)]
res = [0, 0]
recursion()
print(res[0])
print(res[1])
