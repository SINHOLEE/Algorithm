from collections import deque
t = int(input())
for _ in range(t):
    tem = list(map(str, input().split()))
    e = float(tem[0])
    n = int(tem[1])
    N_case = int(input())
    data = []
    for _ in range(N_case):
        temp = list(map(float, input().split()))
        data.append(temp)
    # print()
    # print(e, n)
    # print(data)
    adj_list = [[] for _ in range(N_case)]
    cluster_num = [1] * (N_case)
    eps = [[0] * N_case for _ in range(N_case)]
    adj_list = [[]  for _ in range(N_case)]
    for i in range(N_case):
        for j in range(i+1, N_case):
            if i == j:
                continue
            ans = 0

            for k in range(len(data[0])): # case1 == 4
                ans += (data[i][k] - data[j][k]) ** 2
            ans = ans ** (0.5)
            # print('ans', ans, 'epsilopn', e)
            if ans <= e:
                adj_list[i].append(j)
                adj_list[j].append(i)
                cluster_num[i] += 1
                cluster_num[j] += 1

    a = 0
    # for aa in adj_list:
    #     print(a, aa)
    #     a+=1
    # print(cluster_num)
    dq = deque([])

    visited = [-1] * N_case
    cnt = 0
    for node in range(N_case):
        if cluster_num[node] >= n: # 코어그룹
            if visited[node] == -1:
                dq.append(node)
                visited[node] = cnt
                while dq:
                    v = dq.popleft()

                    for next in adj_list[node]:
                        if visited[next] == -1:
                            if cluster_num[next] >= n:
                                visited[next] = cnt
                                dq.append(next)
                cnt+=1
    print(', '.join(map(str, visited)))
