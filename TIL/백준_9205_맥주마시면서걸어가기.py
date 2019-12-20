from collections import deque
T = int(input())

for _ in range(T):
    n = int(input())
    visited = [0] * (n+2)
    mat = [[0] * (n+2) for _ in range(n+2)]
    end = n+1
    locations = []
    for i in range(n+2):
        a, b = map(int, input().split())
        locations.append((a, b))
        if i == 0:
            continue
        for v in range(i):
            mat[v][i] = abs(locations[v][0]- locations[i][0]) + abs(locations[v][1] - locations[i][1])
            mat[i][v] = abs(locations[v][0] - locations[i][0]) + abs(locations[v][1] - locations[i][1])

    # 완전탐색 버전

    dq = [0]
    visited[0] = 1
    flag = True
    while dq:
        node = dq.pop(0)

        if node == end:
            print('happy')
            flag = False
            break
        for i in range(n+2):
            if visited[i]:
                continue
            if mat[node][i] <= 1000:
                dq.append(i)
                visited[i] = 1
    if flag:
        print('sad')