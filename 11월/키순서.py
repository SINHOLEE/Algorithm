T = int(input())
for t in range(1, T+1):
    n = int(input())
    M = int(input())
    adj_mat = [[999999999] * n for _ in range(n)]
    for m in range(M):
        a, b = map(lambda x:int(x)-1, input().split())
        adj_mat[a][b] = 1
    for i in range(n):
        for j in range(n):
            if i == j:
                adj_mat[i][j] = 0
    for line in adj_mat:
        print(line)

    # 플로이드 워셜 알고리즘 : 전체 숫자를 연결하는 최단거리를 구한다.
    # a->b직접연결시
