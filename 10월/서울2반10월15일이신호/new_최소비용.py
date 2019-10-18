from pprint import pprint

di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]

T = int(input())
for tc in range(1 , T+1):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]

    distance = [[9999999] * n for _ in range(n)]
    distance[0][0] = 0
    cnt = 0
    node = 0
    visited = [[False] * n for _ in range(n)]  # num으로 관리
    visited[0][0] = True
    i = 0
    j = 0
    pq = []
    while True:
        if cnt == n ** 2 - 1:
            break
        for k in range(4):
            new_i = i
            new_j = j
            # print(new_i,new_j)
            if new_i + di[k] >= 0 and  new_i + di[k] <= n -1 and new_j + dj[k] >= 0 and new_j + dj[k] <= n-1 and visited[new_i+di[k]][new_j+dj[k]] == False:
                if mat[new_i][new_j] < mat[new_i+di[k]][new_j+dj[k]]:
                    plus = -(mat[new_i][new_j] - mat[new_i+di[k]][new_j+dj[k]]) + 1
                else:
                    plus = 1
                distance[new_i+di[k]][new_j+dj[k]] = min(distance[new_i+di[k]][new_j+dj[k]], distance[new_i][new_j] + plus)

                if (distance[new_i+di[k]][new_j+dj[k]], new_i+di[k], new_j+dj[k]) in pq:
                    pass
                else:
                    pq.append((distance[new_i+di[k]][new_j+dj[k]], new_i+di[k], new_j+dj[k]))
        pq.sort()
        # print(pq)
        a = pq.pop(0)

        visited[a[1]][a[2]] = True
        i = a[1]
        j = a[2]
        cnt += 1
    print('#%s %s' % (tc, distance[-1][-1]))