from pprint import pprint

def move(i, j, result):
    global min_value
    if i > N - 1 or j > N - 1:
        return
    if i == N - 1 and j == N - 1:
        if min_value > result:
            min_value = result
        return
    if result > min_value:
        return
    if j + 1 < N:
        move(i, j + 1, result + mat[i][j + 1])
    if i + 1 < N:
        move(i + 1, j, result + mat[i + 1][j])


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    # pprint(mat)

    i_index = 0
    j_index = 0
    min_value = 99999999999999999999

    move(i_index, j_index, mat[i_index][j_index])
    print('#%s %s' % (tc, min_value))
