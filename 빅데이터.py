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
    print()
    print(e, n)
    print(data)
    adj_list = [[] for _ in range(N_case)]
    cluster_num = [0] * (N_case)
    eps = [[0] * N_case for _ in range(N_case)]
    adj_mat = [[0]*N_case for _ in range(N_case)]
    for i in range(N_case):
        for j in range(N_case):
            if i == j:
                continue
            ans = 0

            for k in range(len(data[0])): # case1 == 4
                ans += (data[i][k] - data[j][k]) ** 2
            ans = ans ** (0.5)
            # print('ans', ans, 'epsilopn', e)
            if ans < e:
                print()
                adj_mat[i][j] = 1
                cluster_num[i] += 1
                eps[i][j] = ans


    print(cluster_num)

    list()

