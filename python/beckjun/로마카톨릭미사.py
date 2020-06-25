dy = (-1, -1, 0, 1, 1, 1, 0, -1)
dx = (0, 1, 1, 1, 0, -1, -1, -1)
n, m = map(int, input().split())
mat_origin = [list(input()) for _ in range(n)]
ans = 0


def cnt_handshake():
    cnt = 0
    mat = [arr[:] for arr in mat_origin]
    for i in range(n):
        for j in range(m):
            if mat[i][j] == "o":
                mat[i][j] = "."
                for k in range(8):
                    ny, nx = i + dy[k], j + dx[k]
                    if not (0 <= ny < n and 0 <= nx < m):
                        continue
                    if mat[ny][nx] == ".":
                        continue
                    if mat[ny][nx] == "o":
                        cnt += 1
    return cnt


ans = cnt_handshake()
for i in range(n):
    for j in range(m):
        if mat_origin[i][j] == ".":
            mat_origin[i][j] = "o"
            ans = max(ans, cnt_handshake())
            mat_origin[i][j] = "."

print(ans)


