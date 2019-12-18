T = int(input())

for t in range(T):
    n = int(input())
    mat = [[0] * (n+1) for _ in range(n+1)]
    visited = [0] * (n+1)
    temp = list(map(int, input().strip().split()))
    indegree = [0] * (n+1)
    for i in range(len(temp)):
        if i == 0:
            visited[temp[i]] = 1
            continue

        for j in range(1, n+1):
            if not visited[j]:
                mat[temp[i-1]][j] = 1
                indegree[j] += 1
        visited[temp[i]] = 1
    m = int(input())
    for _ in range(m):
        a,b = map(int, input().split())

        # 서로 뒤집힐 경우를 생각해야 하므로
        if mat[b][a]:
            mat[a][b] = 1
            mat[b][a] = 0

            indegree[a] -= 1
            indegree[b] += 1
        else:
            mat[a][b] = 0
            mat[b][a] = 1

            indegree[b] -= 1
            indegree[a] += 1

    stop = False
    dq = []
    visited = [0] *(n+1)
    cnt = 0
    res = [] # 결과담는 버킷
    for num in range(1,n+1):
        if indegree[num] == 0:
            cnt += 1
            dq.append(num)
            visited[num] = 1
            res.append(num)

    if not stop:
        for _ in range(n):
            if len(dq) == 0:
                stop = True
                print('IMPOSSIBLE')
                break
            node = dq.pop(0)
            # 진입차수가 팝한 기준으로 1개 이상이면, 순서를 특정지을 수 없으므로 물음표
            if len(dq) >= 1:
                stop = True
                print('?')
                break
            for j in range(1, n+1):
                if visited[j] == 0 and mat[node][j]:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        dq.append(j)
                        res.append(j)
                        cnt += 1
    if not stop:
        print(' '.join(map(str, res)))


