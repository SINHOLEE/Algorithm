from pprint import pprint
     # 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def iswall(i, j):
    global R, C
    if i < 0 or j < 0 or i > R - 1 or j > C - 1:
        return True
    else:
        return False
R, C, T = map(int, input().split())
mat = []
for i in range(R):
    temp = list(map(int, input().split()))
    mat.append(temp)
dirties = {}
air_cleaner = []
for i in range(R):
    for j in range(C):
        # if mat[i][j] != -1:
        dirties[(i, j)] = (mat[i][j], 0)  # (좌표 i, 좌표j) : 미세먼지 양, 사방에서 받는 먼지의 양
        if mat[i][j] == -1:
            air_cleaner.append((i, j))
# print(len(dirties))
# print(dirties)

# 횟수만큼 돌리기
for t in range(T):


    # 미세먼지 확산
    for key, item in dirties.items():
        #확산하기 위해 5 이상의 먼지만 바라본다.
        if item[0] < 5:
            continue
        clone = item[0] // 5
        i = key[0]
        j = key[1]
        my_dirty = item[0]
        sum_of_clone = item[1]
        # print(key, item)
        #사방을 바라 본다.
        for k in range(4):
            ii = i + di[k]
            jj = j + dj[k]
            if not iswall(ii, jj):
                if mat[ii][jj] == -1:
                    continue
                else:
                    my_dirty -= clone
                    dirties[(ii, jj)] = (dirties[(ii, jj)][0], dirties[(ii, jj)][1] + clone )
                dirties[(i, j)] = (my_dirty, sum_of_clone)
            else:
                pass
    # 전체 합치기
    for key, item in dirties.items():
        dirties[key] = (item[0] + item[1], 0)

    # 가시적 확인
    # new_mat = [[0] * C for _ in range(R)]
    # for key, item in dirties.items():
    #     new_mat[key[0]][key[1]] = item[0]
    # pprint(new_mat)
    # print('위는 바람 불기 전')

    # 공기 청정기 바람불기
    top_cleaner = air_cleaner[0]  # (i, j)
    bottom_cleaner = air_cleaner[1]
                     #우, 상, 좌, 하
    top_direction_i = [0, -1, 0, 1]
    top_direction_j = [1, 0, -1, 0]

    i = top_cleaner[0] + top_direction_i[0]  # 공기청정기에서 우측으로 한칸만 가있어라.
    j = top_cleaner[1] + top_direction_j[0]
    my_queue = []
    my_queue.append(dirties[(i, j)])
    dirties[(i, j)] = (0, 0)
    for kk in range(4):
        # if dirties[(i, j)][0] == -1:
        #     break
        check = True
        while True:
            i += top_direction_i[kk]
            j += top_direction_j[kk]
            if iswall(i, j):
                i -= top_direction_i[kk]
                j -= top_direction_j[kk]
                break
            if dirties[(i, j)][0] == -1:
                check = False
                break
            if check:
                my_queue.append(dirties[(i, j)])
                dirties[(i, j)] = (my_queue.pop(0))

                        # 우 하 좌 상
    bottom_direction_i = [0, 1, 0, -1]
    bottom_direction_j = [1, 0, -1, 0]

    i = bottom_cleaner[0] + bottom_direction_i[0]  # 공기청정기에서 우측으로 한칸만 가있어라.
    j = bottom_cleaner[1] + bottom_direction_j[0]
    my_queue = []
    my_queue.append(dirties[(i, j)])
    dirties[(i, j)] = (0, 0)
    for kk in range(4):
        # if dirties[(i, j)][0] == -1:
        #     break
        check = True
        while True:
            i += bottom_direction_i[kk]
            j += bottom_direction_j[kk]
            if iswall(i, j):
                i -= bottom_direction_i[kk]
                j -= bottom_direction_j[kk]
                break
            if dirties[(i, j)][0] == -1:
                check = False
                break
            if check:
                my_queue.append(dirties[(i, j)])
                dirties[(i, j)] = (my_queue.pop(0))

    # new_mat = [[0] * C for _ in range(R)]
    # for key, item in dirties.items():
    #     new_mat[key[0]][key[1]] = item[0]
    # pprint(new_mat)
    # print()

    # print(dirties[(2, 0)][0])

result = 2
for value in dirties.values():
    result += value[0]

print(result)
# print(dirties)
