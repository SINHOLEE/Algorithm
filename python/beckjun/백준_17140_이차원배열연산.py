r,c,k = map(int,input().split())

mat = [[*map(int, input().split())] for i in range(3)]

r = r-1
c = c-1

cnt = 0
n = 3
m = 3
while cnt <= 100:
    if r < n and c < m and mat[r][c] == k:
        break
    dummy_mat = []
    if n >= m: # r연산
        max_m = 0
        for i in range(n):
            my_lis = [[0, i] for i in range(101)]
            for j in range(m):
                if mat[i][j] == 0:
                    continue
                my_lis[mat[i][j]][0] += 1
            my_lis = sorted([*filter(lambda x: x[0] > 0, my_lis)])
            A = sum(map(lambda x: [x[1], x[0]], my_lis), [])
            if max_m < len(A):
                max_m = len(A)

            # 합치기
            dummy_mat.append(A)
        # 0 추가
        for i in range(n):
            dummy_mat[i] += [0] * (max_m - len(dummy_mat[i]))
        mat = dummy_mat
        m = max_m
        # print(mat)
    else: # c 연산
        max_n = 0
        for i in range(m):
            my_lis = [[0, i] for i in range(101)]
            for j in range(n):
                if mat[j][i] == 0:
                    continue
                my_lis[mat[j][i]][0] += 1
            my_lis = sorted([*filter(lambda x: x[0] > 0, my_lis)])
            A = sum(map(lambda x: [x[1], x[0]], my_lis), [])
            if max_n < len(A):
                max_n = len(A)

            # 합치기
            dummy_mat.append(A)
        for i in range(m):
            dummy_mat[i] += [0] * (max_n - len(dummy_mat[i]))
        # T
        mat = [[0] * m for _ in range(max_n)]
        for i in range(m):
            for j in range(max_n):
                mat[j][i] = dummy_mat[i][j]
        n = max_n

    cnt += 1

if cnt <= 100:
    print(cnt)
else:
    print(-1)