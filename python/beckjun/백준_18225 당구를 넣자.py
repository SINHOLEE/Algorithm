m, n, sx, sy, dx, dy = map(int, input().split())
ox, oy = sx, sy



z = ((oy * m) - (ox * n)) / ((dx * n) - (dy * m))

print(z)