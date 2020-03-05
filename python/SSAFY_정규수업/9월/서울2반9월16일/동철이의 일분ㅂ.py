from pprint import pprint

def perm(num, re):
    global row, max_prop, cnt
    cnt += 1
    if re < max_prop:
        return

    if re == 0:
        return

    if False not in visited:

        if max_prop < re :
            max_prop = re

        return


    for j in range(N):
        if visited[j] == False:
            row += 1

            # if re * (mat[row][j] / 100 ) < max_prop:
            #     row -= 1
            #     continue
            visited[j] = True
            perm(j, re * mat[row][j] / 100)

            visited[j] = False
            row -= 1



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = []
    for n in range(N):
        temp = list(map(int, input().split()))
        mat.append(temp)


    max_prop = 0.0000000000000000000000000000000000000000000000000000000000001
    visited = [False] * N
    cnt = 0
    for i in range(N):

        row = 0
        visited[i] = True

        perm(i, mat[row][i] / 100)
        visited[i] = False
    print('#%s %0.6f' % (tc, max_prop * 100), cnt)


    # pprint(mat)