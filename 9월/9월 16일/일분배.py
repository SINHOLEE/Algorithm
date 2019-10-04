def perm(num, re):
    global max_prop, count

    if re < max_prop:
        return

    if re == 0:
        return

    if count == N:
        if max_prop < re:
            max_prop = re
        return

    for j in range(N):
        if visited[j] == False:
            if re == 0:
                continue
            count += 1
            visited[j] = True
            perm(num + 1, re * mat[num+1][j] / 100)
            visited[j] = False
            count -= 1


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    mat = []
    for n in range(N):
        temp = list(map(int, input().split()))
        mat.append(temp)

    max_prop = 0.0000000000000000000000000000000000000000001
    visited = [False] * N
    count = 0
    for i in range(N):
        visited[i] = True
        count += 1
        perm(0, mat[0][i] / 100)
        visited[i] = False
        count -= 1
    print('#%s %0.6f' % (tc, max_prop * 100))