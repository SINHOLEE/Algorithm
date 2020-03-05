from pprint import pprint

T = int(input())

def iswall(i, j, N):  # 만약 가려는 방향이 벽이면 True반환 / 가도 되면 Flase반환
    if i < 0 or i > N - 1 or j < 0 or j > N - 1:
        return True
    else:
        return False

    # 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
for tc in range(1, T+1):
    N = int(input())
    mat = []
    visited = [[False] * N for _ in range(N)]
    for n in range(N):
        temp = list(map(int, list(input())))
        mat += [temp]
        for t in range(len(temp)):

            if temp[t] == 2:
                start_i = n
                start_j = t

    # pprint(visited)
    # pprint(mat)
    #
    i = start_i
    j = start_j
    count = 0
    my_queue = []
    # while mat[i][j] != 3 and len(my_queue) != 0:

    check = False
    my_queue.append([i, j, count])
    while True:
        if check:
            # print('c')
            break

        if len(my_queue) == 0:
            # print('len 0')
            break



        temp = my_queue.pop(0)  # temp = [i, j, count]

        visited[temp[0]][temp[1]] = True  # 현재 위치에 방문했으므로 체크

        for k in range(4):  # 현재 위치(temp[0], temp[1])에서 네 방향을 조사한다.
            if not iswall(temp[0] + di[k], temp[1] + dj[k], N):  # 네방향을 바라보는데 일단 벽이 아니면 좋다.

                if visited[temp[0] + di[k]][temp[1] + dj[k]] == 0 and mat[temp[0] + di[k]][temp[1] + dj[k]] != 1:  # 길이 있으면 모두 queue에 담고,
                    if mat[temp[0] + di[k]][temp[1] + dj[k]] == 3:
                        check = True
                        # print('chec')
                        count = temp[2]
                        break
                    my_queue.append([temp[0] + di[k], temp[1] + dj[k], temp[2] + 1])  # 내 큐에 모두 담어!
    print('#{} {}'.format(tc, count))




            #     mat[i+di[k]][j+dj[k]] == 0 and   # 4방향을 탐색하면서 일단 벽이 아니고, 0인이면서 방문한 적이 없으면
            #     my_queue.append([i+di[k], j+dj[k]])
            # else:  # 만약 4방향을 바라보면서 0이 아니라며
