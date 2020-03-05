m, n, sx, sy, dx, dy = map(int, input().split())
c = 0
ox, oy = sx, sy
bounce = 0
while True:


    if sx % m == 0 and sy % n == 0:
        print(sx // m + sy // n - 1)
        break
    sx += dx
    sy += dy
