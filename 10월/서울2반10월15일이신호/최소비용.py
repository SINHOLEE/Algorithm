import heapq

di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]

T = int(input())
for tc in range(1 , T+1):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    dic_ij = {}
    dic_num = {}
    cnt = 0
    for i in range(n):
        for j in range(n):
            dic_ij[(i, j)] = cnt
            dic_num[cnt] = (i, j)
            cnt+=1

    distance = [9999999] * (n**2)
    distance[0] = 0
    cnt = 0
    node = 0
    visited = [False] * (n ** 2)  # num으로 관리
    visited[0] = True
    h = []
    while True:
        if cnt == n **2 - 1:
            break
        for k in range(4):
            new_i = dic_num[node][0]
            new_j = dic_num[node][1]

            # print(new_i,new_j)
            if new_i + di[k] >= 0 and  new_i + di[k] <= n -1 and new_j + dj[k] >= 0 and new_j + dj[k] <= n-1 and visited[dic_ij[new_i+di[k], new_j+dj[k]]] == False:
                if mat[new_i][new_j] < mat[new_i+di[k]][new_j+dj[k]]:
                    plus = -(mat[new_i][new_j] - mat[new_i+di[k]][new_j+dj[k]]) + 1
                else:
                    plus = 1


                distance[dic_ij[(new_i+di[k], new_j+dj[k])]] = min(distance[dic_ij[(new_i+di[k], new_j+dj[k])]], distance[dic_ij[(new_i), new_j]] + plus)
                if distance[dic_ij[(new_i + di[k], new_j + dj[k])]] == 9999999:
                    continue
                if (distance[dic_ij[(new_i + di[k], new_j + dj[k])]], new_i + di[k], new_j + dj[k]) in h:
                    pass
                else:
                    heapq.heappush(h,(distance[dic_ij[(new_i + di[k], new_j + dj[k])]], new_i + di[k], new_j + dj[k]))
        a = heapq.heappop(h)
        print(a)
        node = dic_ij[(a[1], a[2])]
        visited[node] = True
        cnt += 1
    print('#%s %s' % (tc, distance[-1]))