from pprint import pprint

T = int(input())

def abs_length(x1, y1, x2, y2):
    if x1 >= x2:
        a = x1 - x2

    else:
        a = x2 - x1

    if y1 >= y2:
        b = y1 - y2
    else:
        b = y2 - y1

    return a + b

def DFS(m):
    global currents, N, min_path, visited
    visited[m] = True
    currents.append(m)



    for i in range(len(linked_mat[m])):
        if linked_mat[m][i] == 1 and visited[i] == False:

            DFS(i)
            visited[i] = False
            currents.pop()
# print(abs_length(10, 20, 30, 40))

for tc in range(1, T+1):
    N = int(input())

    temp = list(map(int, input().split()))
    # print(temp)
    company = []
    home = []
    clients = []
    for t in range(0, len(temp) - 1, 2):
        if t == 0:
            company += [temp[t], temp[t + 1]]
        elif t == 2:
            home += [temp[t], temp[t + 1]]
        else:
            clients.append([temp[t], temp[t + 1]])
    # print(company)
    # print(home)
    linked_mat = [[0] * N for _ in range(N)]


    for i in range(N):
        for j in range(N):
            if i == j:
                pass
            else:
                linked_mat[i][j] = 1

    # pprint(linked_mat)
    # pprint(visited)
    min_path = 100000000000  # 최소거리


    for i in range(N):
        visited = [False] * N
        currents = []

        DFS(i)
    # for i in range(N):
    #     visited = [False] * N
    #
    #     DFS(i)
    #     print(i)
    print('#{} {}'.format(tc, min_path))