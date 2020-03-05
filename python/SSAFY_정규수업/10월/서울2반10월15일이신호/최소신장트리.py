from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    keys = [9999999] * (V+1)
    pi = [-1] *(V+1)
    mat = [[0] *(V+1) for _ in range(V+1)]
    for e in range(E):
        v1, v2, cost = map(int, input().split())
        mat[v1][v2] = cost
        mat[v2][v1] = cost
    # 시작점 0으로 잡자.
    visited = [False] * (V+1)
    target = 0
    visited[0] = True
    keys[0] = 0
    cnt = 0
    while True:
        if cnt == V:
            break
        # 1 연결 하기
        for i in range(len(mat[target])):
            if visited[i] == False and mat[target][i] != 0:
                if keys[i] > mat[target][i]:
                    keys[i] = mat[target][i]
                    pi[i] = target
        min_idx = -1
        my_min = 99999999999
        for i in range(V+1):
            if visited[i] == False and my_min > keys[i]:
                my_min = keys[i]
                min_idx = i
        target = min_idx
        visited[target] = True
        cnt += 1
    print('#%s %s' % (tc, sum(keys)))