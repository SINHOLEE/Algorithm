from pprint import pprint

T = int(input())

def iswall(i, j, N):  # 만약 가려는 방향이 벽이면 True반환 / 가도 되면 Flase반환
    if i < 0 or i > N or j < 0 or j > N:
        return True
    else:
        return False

    # 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
for tc in range(1, T+1):
    N = int(input())
    mat = []
    visited = []
    for n in range(N):
        temp = list(map(int, list(input())))
        mat += [temp]
        new = []
        for t in range(len(temp)):

            if temp[t] == 2:
                start_i = n
                start_j = t
                new.append(0)
            else:
                new.append(temp[t])
        visited += [new]

    pprint(visited)
    pprint(mat)
    #
    i = start_i
    j = start_j
    count = 0
    my_queue = []
    while mat[i][j] != 3 and len(my_queue) != 0:
        count += 1
        for k in range(4):
            if not iswall(i+di[k], j+dj[k], N):  # 네방향을 바라보는데 일단 벽이 아니면 좋다.
                if mat[i+di[k]][j+dj[k]] == 0 or mat[i+di[k]][j+dj[k]] == 3:  # 길이 있으면 모두 queue에 담고,
                    my_queue.append([i+di[k], j+dj[k]])  # 내 큐에 모두 담어!

                else: # 벽이 없어도 바라보는 방향에 1이 있으므로 죽어
                    pass
            else:  # 벽이면 죽어
                pass

        # 큐를 다 담고 while문을 돌거야 이게 깊어질때 마다 미로의 거리를 판단할 수 있게 돼!
        while my_queue: # queue가 없어질때까지 계속 pop(0)한다.

            point = my_queue.pop(0)
            if visited[point[0]][point[1]] == 0:
                i = point[0]
                j = point[1]
            else:
                pass
            



            #     mat[i+di[k]][j+dj[k]] == 0 and   # 4방향을 탐색하면서 일단 벽이 아니고, 0인이면서 방문한 적이 없으면
            #     my_queue.append([i+di[k], j+dj[k]])
            # else:  # 만약 4방향을 바라보면서 0이 아니라며
