from pprint import pprint

def perm(depth, temp):
    global N, result, count
    count += 1
    if depth == N:
        if result > temp:
            result = temp
        return

    # if temp > result:
    #     return

    for i in range(N):
        if visited[i] == False:
            if temp + mat[depth][i] > result:
                continue

            visited[i] = True
            perm(depth+1, temp + mat[depth][i])
            visited[i] = False
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    result = 100000000000000000
    visited = [False] * N
    count = 0
    perm(0, 0)
    print('#%s %s' % (tc, result))