def schedule(i, depth):
    global max_count, count
    count += 1
    
    start = time_schedule[i][0]
    end = time_schedule[i][1]
    
    visited[start:end] = [True] * len(visited[start:end])
    if max_count < depth:
        max_count = depth

    for j in range(i, N):  # i 부터 시작해야지 이전에 거쳐왔던 정보를 다시 안 훝는다
        start_j = time_schedule[j][0]
        end_j = time_schedule[j][1]
        if True not in visited[start_j:end_j]:  # start:end
            schedule(j, depth+1)
            visited[start_j:end_j] = [False] * len(visited[start_j:end_j])



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    time_schedule = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x:x[-1])  # 중요!! 끝점을 기준으로!!
    index_str = [str(x) for x in range(N)]
    visited = [0] * 25

    max_count = 0
    # 횟수구해보자
    count = 0
    depth = 0
    # 러프한 최대값 찾기

    schedule(0, depth + 1)  # index, depth
    start = time_schedule[0][0]
    end = time_schedule[0][1]
    visited[start:end] = [False] * len(visited[start:end])

    print('#%s %s' % (tc, max_count))
