T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    mat = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        mat.append(temp)

    max_fly = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            flies = 0
            for ii in range(i, i + M):
                for jj in range(j, j + M):
                    flies += mat[ii][jj]
            if max_fly <= flies:
                max_fly = flies
    print('#%s %d' % (tc, max_fly))
