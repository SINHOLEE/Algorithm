T = int(input())
# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    # print(mat)

    max_count = 1
    max_Aij = -1
    for i in range(N):
        for j in range(N):
            count = 1
            # if max_count > N ** 2 - mat[i][j]:  # 가지치기
            #     continue
            flag = True
            start_Aij = mat[i][j]
            while True:
                if flag == False:
                    break
                cnt = 0
                for k in range(4):
                    ii = i + di[k]
                    jj = j + dj[k]
                    if i + di[k] >= 0 and j + dj[k] >= 0 and i + di[k] <= N - 1 and j + dj[k] <= N - 1 and mat[i][j] + 1 == mat[i + di[k]][j + dj[k]]:
                        count += 1
                        cnt += 1
                        i += di[k]
                        j += dj[k]
                        break
                if cnt == 0:
                    flag = False
                    if max_count < count:
                        max_count = count
                        max_Aij = start_Aij
                    elif max_count == count:
                        if max_Aij < start_Aij:
                            pass
                        else:
                            max_Aij = start_Aij
    print('#%s %s %s' % (tc, max_Aij, max_count))