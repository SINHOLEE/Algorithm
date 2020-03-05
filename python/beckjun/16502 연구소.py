import copy
from pprint import pprint
    # 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def iswall(i, j):
    global row, col

    if i < 0 or j < 0 or i > row - 1 or j > col - 1:
        return True
    else:
        return False

def spead_birus(matrix):
    my_stack = []
    co_visited = copy.deepcopy(visited)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 2:
                for k in range(4):
                    ii = i + di[k]
                    jj = j + dj[k]
                    if not iswall(ii, jj) and co_visited[ii][jj] == False and matrix[ii][jj] == 0:
                        my_stack.append([ii, jj])


                while True:
                    if not my_stack:
                        break

                    v = my_stack.pop()
                    iii = v[0]
                    jjj = v[1]
                    if co_visited[iii][jjj] == False:
                        co_visited[iii][jjj] = True
                        matrix[iii][jjj] = 2
                    else:
                        continue



                    for a in range(4):
                        iiii = iii + di[a]
                        jjjj = jjj + dj[a]
                        if not iswall(iiii, jjjj) and co_visited[iiii][jjjj] == False and matrix[iiii][jjjj] == 0:
                            my_stack.append([iiii, jjjj])

    return matrix
def zero_count(matrix2):
    global row, col

    count = 0
    for i in range(row):
        for j in range(col):
            if matrix2[i][j] == 0:
                count += 1
    return count

def make_three_walls(matrix1):
    global row, col, max_zero

    bucket = []
    for i in range(row):
        for j in range(col):
            if matrix1[i][j] == 0:
                bucket.append([i, j])
    for a in range(len(bucket)):
        for b in range(a + 1, len(bucket)):
            for c in range(b + 1, len(bucket)):
                co_mat = copy.deepcopy(matrix1)
                # print(bucket[a], bucket[b], bucket[c])
                # # pprint(co_mat)
                # # print('기초')
                co_mat[bucket[a][0]][bucket[a][1]] = 1
                co_mat[bucket[b][0]][bucket[b][1]] = 1
                co_mat[bucket[c][0]][bucket[c][1]] = 1
                # pprint(co_mat)
                # print('벽세운 후')
                co_mat = spead_birus(co_mat)
                # pprint(co_mat)
                # print('세균번식 후')
                current_count = zero_count(co_mat)
                # print('--------------------------------', current_count)
                if max_zero < current_count:
                    max_zero = current_count
                    # pprint(co_mat)
                    # print('세균번식후인데//')
                    # print(max_zero)
                    # print()

#
#
row, col = map(int, input().split())

mat = []
visited = []
for r in range(row):
    temp = list(map(int, input().split()))
    v = [False] * col
    visited.append(v)
    mat.append(temp)

max_zero = 0
make_three_walls(mat)

print(max_zero)


