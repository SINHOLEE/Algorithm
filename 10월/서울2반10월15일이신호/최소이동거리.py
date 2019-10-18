from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    n, e = map(int, input().split())
    d = [999999] * (n+1)

    mat = [[0] * (n + 1) for _ in range(n+1)]

    for E in range(e):
        s,e,w = map(int, input().split())
        mat[s][e] = w
    distance = [999999] * (n+1)
    distance[0] = 0
    target = n
    node = 0
    visited = [False] * (n+1)
    visited[0] = True
    while True:
        if node == target:
            break
        for i in range(len(mat[node])):
            if visited[i] == False and mat[node][i] != 0:
                distance[i] = min(distance[i], distance[node] + mat[node][i])

        min_val = 99999999
        for j in range(len(distance)):
            if visited[j] == False and min_val > distance[j]:
                min_val = distance[j]
                node = j
        visited[node] = True

    print('#%s %s' % (tc, distance[target]))