near = ((0,1),(0,-1),(1, 0),(-1, 0),(1,1),(-1,1),(1,-1),(-1,-1))

T = int(input())
for t in range(1,T+1):
    n = int(input())
    mat = [list(map(lambda x: 0 if x == '.' else  -1, input())) for _ in range(n)]
    for a in mat:
        print(a)
    dummy_mat = [arr[:] for arr in mat]
    for i in range(n):
        for j in range(n):
            if mat[i][j] == -1:
                for dy, dx in near:
                    newY, newX = i + dy, j + dx
                    if not (0<=newY<n and 0<=newX<n):
                        continue
                    if mat[newY][newX] == -1:
                        continue
                    mat[newY][newX] = 1
    print()

    for a in mat:
        print(a)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 0:
                cnt += 1
                mat[i][j] = cnt
                q = [(i, j)]
                while q:
                    y, x = q.pop(0)
                    for dy, dx in near:
                        newY, newX = i + dy, j + dx
                        if not (0 <= newY < n and 0 <= newX < n):
                            continue
                        if dummy_mat[newY][newX] == 0:


                            cnt -= 1
                            continue

                        dummy_mat[newY][newX] = cnt
    print('wlfhl')
    print(cnt)
    for a in dummy_mat:
        print(a)

    for i in range(n):
        for j in range(n):
            if dummy_mat[i][j] == 0:
                cnt += 1
    print('#%s %s' % (t, cnt))