

def IsCamical(i, j):
    global N
    if i < 1 or j < 1 or i >= N - 1 or j >= N - 1:
        return True
    else:
        return False
def scan(group):
    global N

    # 약품에 닿았는지 검사 + 없어지는 것
    new_group = []
    for x in range(len(group)):
        i = group[x][0]  # 좌표 i
        j = group[x][1]  # 좌표 j
        if IsCamical(i, j):
            cell = group[x][2] // 2
            if cell == 0:
                pass
            else:
                if group[x][3] == 1:
                    new_group.append([i, j, cell, 2])
                elif group[x][3] == 2:
                    new_group.append([i, j, cell, 1])
                elif group[x][3] == 3:
                    new_group.append([i, j, cell, 4])
                elif group[x][3] == 4:
                    new_group.append([i, j, cell, 3])
        else:
            cell = group[x][2]
            new_group.append([i, j, cell, group[x][3]])
    # print('asdasdsada')
    # 합쳐지는 것 검사.
    visited = [False] * len(new_group)
    result = []

    #
    for ii in range(len(new_group)):
        if visited[ii] == True:
            continue
        visited[ii] = True
        a = new_group[ii]
        temp1 = []
        check = True
        for jj in range(len(new_group)):
            if ii < jj:
                if visited[jj] == False and new_group[ii][0] == new_group[jj][0] and new_group[ii][1] == new_group[jj][1]:
                    visited[jj] = True
                    temp1.append(new_group[jj])
                    check = False

        if check and visited[ii] == False:
            result.append(a)
        else:
            temp1.append(a)
            cell1 = sum([temp1[i][2] for i in range(len(temp1))])
            direction1 = sorted(temp1)[-1][3]
            temp2 = [temp1[0][0], temp1[0][1], cell1, direction1]
            result.append(temp2)
    return result

def move(object):
            #상 하  좌  우
    di = [False, -1, 1, 0, 0]

    dj = [False, 0, 0, -1, 1]

    i = object[0] + di[object[3]]
    j = object[1] + dj[object[3]]
    return [i, j, object[2], object[3]]




def count_cells(group):
    pass

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    group = []
    for _ in range(K):
        object = list(map(int, input().split()))  # [i, j, nums_of_cell, direction]
        group.append(object)
    for m in range(M):
        for obj in range(len(group)):
            group[obj] = move(group[obj])  # 한 미생물씩 움직인다.
            # print(group[obj])

        group = scan(group)
    total = 0
    for g in range(len(group)):
        total += group[g][2]

    print('#%s %d' % (tc, total))

