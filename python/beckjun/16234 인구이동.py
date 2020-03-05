from pprint import pprint
import copy
def iswall(i, j):
    global N
    if i < 0 or j < 0 or i > N - 1 or j > N - 1:
        return True
    else:
        False
    # 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
N, L, R = map(int, input().split())

mat = []
real_visited = []
for n in range(N):
    temp = list(map(int, input().split()))
    mat.append(temp)
    temp1 = [0] * N
    real_visited.append(temp1)


countries = []
for ii in range(N):
    for jj in range(N):
        countries.append((ii, jj, mat[ii][jj]))

# print(countries)
#
# print(visited)

nums_of_move = 0
name_of_union = -1
while True:
    visited = copy.deepcopy(real_visited)
    name_of_union = 0
    my_queue = []
    dic = {}
    for i in range(len(countries)):
        if visited[countries[i][0]][countries[i][1]] != 0:
            continue
        else:
            my_queue.append(countries[i])  # 여러번 훑을거기 때문에

            name_of_union += 1
        nums_of_board = 0
        population = 0

        while True:
            if not my_queue:
                break
            country = my_queue.pop(0)  # (i, j, 인구수)
            if visited[country[0]][country[1]] == name_of_union:
                continue
            visited[country[0]][country[1]] = name_of_union  # 연합이름
            population += mat[country[0]][country[1]]  # 이번 연합의 총 인구수
            if dic.get(name_of_union):
                dic[name_of_union].append((country[0], country[1], mat[country[0]][country[1]]))
            else:
                dic[name_of_union] = [(country[0], country[1], mat[country[0]][country[1]])]
            # print(dic)
            for k in range(4):
                i = country[0] + di[k]
                j = country[1] + dj[k]

                if not iswall(i, j):


                    if abs(mat[country[0]][country[1]] - mat[i][j]) >= L and abs(mat[country[0]][country[1]] - mat[i][j]) <= R:  # 국경을 열 조건
                        if visited[i][j] == name_of_union:
                            nums_of_board += 1
                            # print('----')
                            # print(country[0], country[1])
                            # print(i, j, nums_of_board)
                            # print(name_of_union, population)
                            # print('--')
                        else:
                            my_queue.append((i, j))
                    else:
                        pass

                else:
                    pass
        dic[name_of_union].append(population)
    # print(dic)
    count = 0
    # print(dic)
    for key, item in dic.items():
        if len(item) == 2:
            if mat[item[0][0]][item[0][1]] == item[1]:
                count += 1
                mat[item[0][0]][item[0][1]] = item[1]

            else:
                mat[item[0][0]][item[0][1]] = item[1]
        else:
            people = item[-1] // (len(item) - 1)
            for r in range(len(item) - 1):
                if mat[item[r][0]][item[r][1]] == people:
                    count += 1
                else:
                    mat[item[r][0]][item[r][1]] = people
    # pprint(mat)


    if name_of_union == (N * N):
        break
    nums_of_move += 1

# print()
print(nums_of_move)
