from pprint import pprint

# 행렬리스트로 풀기
def DFS(m):
    global count, max_count, N
    if max_count <= count:
        max_count = count

    visited[m] = 1
    count += 1
    if visited[m] == 0:
        visited[m] = 1
    else:
        pass

    for i in range(1, N + 1):
        if mat[m][i] == 1 and visited[i] == 0:
            DFS(i)
            count -= 1









T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N 정점의 개수, M 간선의 개수
    mat = []
    mat = [[0] * (N + 1) for _ in range(N + 1)]
    if_0_start = [0] * (N + 1)
    for _ in range(M):
        my_line = list(map(int, input().split()))
        if_0_start[my_line[1]] = 1
        mat[my_line[0]][my_line[1]] = 1
        mat[my_line[1]][my_line[0]] = 1
    max_list = []
    max_count = 0
    visited = [0] * (N + 1)
    count = 0
    for j in range(1, N + 1):
        if if_0_start[j] == 0:

            if visited[j] == 0:
                DFS(j)

    print('#{} {}'.format(tc, max_count+1))

    # my_stack = [0] * 100
    # top = -1
    # count = 0
    # max_count = 0
    # min_count = 0
    #
    # # 간선은 무방향성이므로, 양 방향 모두 체크해야 한다.

    #
    # # 모든 정점에 대해 조사해보자.
    # for i in range(1, N + 1):
    #     if visited[i] == 0:
    #         visited[i] = 1
    #
    #     for j in range(1, N + 1):
    #         if mat[i][j] == 1 and visited[j] == 0:
    #             mat[i][j] = 0  # 모든 정점을 조사하는 도중 한번 들렀으므로 다시 안들리게 0으로 변환하자
    #
    #             # 간선 i->j 방향 push()
    #             top += 1
    #             my_stack[top] = j
    #             # j가 1부터 N + 1 까지 다 돌때까지, mystack에 차곡 차곡 쌓는다.
    #     while True:
    #         if top == -1:
    #             break
    #         # pop()
    #         top -= 1
    #         v = my_stack[top]
    #
    #         if visited[v]:  # 만약 내가 조사하는 정점이 이전에 들렀었다면,
    #             count -= 1
    #
    #         else:  # 만약 pop 한 v 정점이 이전에 들르지 않았더라면,
    #             visited[v] = 1
    #             count += 1
    #
    #         if max_count < count:
    #             max_count = count
    #         if min_count > count:
    #             min_count = count
    #
    # if max_count == 0:
    #     if min_count == 0:
    #         result = 1
    #     else:
    #         result = (min_count * -1) + 1
    # else:
    #     if min_count == 0:
    #         result = max_count + 1
    #     else:
    #         result = max_count - min_count + 1
    #
    # print('#{} {}'.format(tc, result))
