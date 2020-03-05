from pprint import pprint

# T = int(input())
#
#      #상 하 좌 우
# di = [-1, 1, 0, 0]
# dj = [0, 0, -1, 1]
# for tc in range(1, T+1):
#     N = int(input())
#     mat = [[1] * (N + 2) for _ in range(N + 2)]
#     visited = [[1] * (N + 2) for _ in range(N + 2)]
#     start_index = []
#     for ii in range(1, N + 1):
#         temp = input()
#         for jj in range(1, N + 1):
#
#             if int(temp[jj - 1]) == 2:
#                 start_index = [ii, jj]
#             mat[ii][jj] = int(temp[jj - 1])
#             if int(temp[jj - 1]) == 3:
#                 visited[ii][jj] = 0
#             else:
#                 visited[ii][jj] = int(temp[jj - 1])
#
#     i = start_index[0]
#     j = start_index[1]
#     top = -1
#     mystack = [[]] * 50
#     while True:
#         if mat[i][j] == 3:
#             print('#{} 1'.format(tc))
#             break
#
#         visited[i][j] = 4
#         for d in range(4):
#             if visited[i + di[d]][j + dj[d]] == 0:
#                 top += 1
#                 mystack[top] = [i + di[d], j + dj[d]]
#
#         if top == -1:
#             print('#{} 0'.format(tc))
#             break
#         # pop
#         elem = mystack[top]
#         top -= 1
#         if visited[elem[0]][elem[1]] == 0:
#             i = elem[0]
#             j = elem[1]

    # top += 1
    # mystack[top] = [1, 2]
    # print(mystack, top)
    # pprint(visited)
    #


# 재귀로 찾는 방법

def find_map(x, y, vis):
    global result
    # 상 하 좌 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    if mat[x][y] == 3:
        result = 1
        return 0
    for k in range(3, -1, -1):
        if visited[x + di[k]][y + dj[k]] == 0:
            visited[x + di[k]][y + dj[k]] = 1
            find_map(x + di[k], y + dj[k], vis)

T = int(input())

for tc in range(1, T+1):
    result = 0
    N = int(input())
    mat = [[1] * (N + 2) for _ in range(N + 2)]
    visited = [[1] * (N + 2) for _ in range(N + 2)]
    start_index = []
    for ii in range(1, N + 1):
        temp = input()
        for jj in range(1, N + 1):

            if int(temp[jj - 1]) == 2:
                start_index = [ii, jj]
            mat[ii][jj] = int(temp[jj - 1])
            if int(temp[jj - 1]) == 3:
                visited[ii][jj] = 0
            else:
                visited[ii][jj] = int(temp[jj - 1])
    pprint(visited)

    find_map(start_index[0], start_index[1], visited)
    if result:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))
