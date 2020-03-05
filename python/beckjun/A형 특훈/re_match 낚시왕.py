
    # 상 하 우 좌
di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]

r, c, m = map(int, input().split())

sharkes = {}
for _ in range(m):
    i, j, s, d, z = map(int, input().split())
    sharkes[(i, j)] = [s, d-1, z]

total = 0
for col in range(1, c+1):
    # catch
    for i in range(1, r+1):
        if sharkes.get((i, col)) != None:
            total += sharkes[(i, col)][2]
            del(sharkes[(i, col)])
            break

    # move
    new_sharkes = {}
    for k, v in sharkes.items():
        i = k[0]
        j = k[1]
        s = v[0]
        d = v[1]
        z = v[2]

        speed = 0
        while True:
            if speed == s:
                break
            if i + di[d] < 1 or i + di[d] > r or j + dj[d] < 1 or j + dj[d] > c:
                d ^= 1
            i += di[d]
            j += dj[d]
            speed += 1

        if new_sharkes.get((i, j)) == None:
            new_sharkes[(i, j)] = [s, d, z]
        else:
            if new_sharkes[(i, j)][2] < z:
                new_sharkes[(i, j)] = [s, d, z]
        sharkes = new_sharkes
print(total)

