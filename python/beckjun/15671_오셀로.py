n = int(input())
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]


def dfs(horse, i, j, d):
    ni, nj = i+di[d], j+dj[d]
    if not (0 <= ni < 6 and 0 <= nj < 6) or mat[ni][nj] == '.':
        return False
    if mat[ni][nj] == horse:
        return True
    if dfs(horse, ni, nj, d):
        mat[ni][nj] = horse
        return True
    return False


mat = [["."] * 6 for _ in range(6)]
mat[2][2], mat[3][3] = 'W', 'W'
mat[2][3], mat[3][2] = 'B', 'B'
for i in range(n):
    r, c = map(int, input().split())
    for d in range(8):
        mat[r-1][c-1] = "W" if i % 2 else "B"
        dfs("W" if i % 2 else "B", r-1, c-1, d)

for a in mat:
    print("".join(map(str, a)))
cnt = 0
for i in range(6):
    for j in range(6):
        if mat[i][j] == 'W':
            cnt += 1
        if mat[i][j] == 'B':
            cnt -= 1

print("White" if cnt > 0 else "Black")
