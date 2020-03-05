# TSP문제

from pprint import pprint
def perm(a, b, temp, cnt):
    global min_elect, how_many
    how_many += 1
    if cnt == N - 1:
        temp += mat[b][0]
        if min_elect > temp:
            min_elect = temp
        return
    #
    # if min_elect < temp:
    #     return

    for j in range(1, N):
        if visited[j]:
            continue
        visited[j] = True
        perm(b, j, temp + mat[b][j], cnt + 1)
        visited[j] = False
T = int(input())

for tc in  range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    # pprint(mat)

    visited = [True] + [False] * N

    min_elect = 999999999999999999999999999
    for i in range(1, N):
        # print(i)
        visited[i] = True
        count = 0
        how_many = 0
        perm(0, i, mat[0][i], count + 1)
        visited[i] = False
    print('#%s %s %s' % (tc, min_elect, how_many))