import time

start = time.time()
R, C, m = tuple(map(int, input().split()))
dr, dc = [0, -1, 1, 0, 0], [0, 0, 0, 1, -1]
reverse_dir = [0, 2, 1, 4, 3]

sharks = {}
pos = [[-1 for _ in range(C)] for _ in range(R)]

for mm in range(1, m+1):
    sharks[mm] = tuple(map(int, input().split()))
    pos[sharks[mm][0] - 1][sharks[mm][1] - 1] = mm

re = 0

for depth in range(R):
    if pos[depth][0] != -1:
        re += sharks[pos[depth][0]][4]
        del sharks[pos[depth][0]]
        pos[depth][0] = -1
        break
for col in range(1, C):
    # move
    eaten = []
    pos_tmp = [[-1 for _ in range(C)] for _ in range(R)]
    for k in sharks.keys():
        r, c, s, d, z = sharks[k]

        c += (dc[d] * s) % (2 * (C - 1))
        r += (dr[d] * s) % (2 * (R - 1))

        for _ in range(2):
            if c < 1:
                c = 2 - c
                d = reverse_dir[d]
            elif c > C:
                c = 2 * C - c
                d = reverse_dir[d]
            elif r < 1:
                r = 2 - r
                d = reverse_dir[d]
            elif r > R:
                r = 2 * R - r
                d = reverse_dir[d]

        sharks[k] = (r, c, s, d, z)
        if pos_tmp[r - 1][c - 1] != -1:
            other = pos_tmp[r - 1][c - 1]
            if z > sharks[other][4]:
                eaten.append(other)
                pos_tmp[r - 1][c - 1] = k
            else:
                eaten.append(k)
        else:
            pos_tmp[r - 1][c - 1] = k
    for e in eaten:
        del sharks[e]
    pos = pos_tmp

    # catch
    for depth in range(R):
        if pos[depth][col] != -1:
            re += sharks[pos[depth][col]][4]
            del sharks[pos[depth][col]]
            pos[depth][col] = -1
            break

    if len(sharks) == 0:
        break

print(re)
print('t', time.time() - start)