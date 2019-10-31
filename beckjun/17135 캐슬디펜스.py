from pprint import pprint
import copy
n, m, d = map(int, input().split())

di = [0, -1, 1]
dj = [-1, 1, 1]
def find_kill(i, j):
    # d 까지 관리하라
    flag = False
    for dd in range(1, d+1):
        new_i = i
        new_j = j
        for k in range(3):
            for ddd in range(dd):
                if (new_i + di[k] < 0 or new_i + di[k] > n-1 or new_j +dj[k] < 0 or new_j +dj[k] > m-1) and new_i +di[k] < i: # 벽이니 패스
                    pass
                else:
                    if mat[new_i+di[k]][new_j+dj[k]]:
                        tem.add((new_i+di[k], new_j+dj[k]))
                        flag = True
                        break
                new_i += di[k]
                new_j += dj[k]
            if flag:
                break
        if flag:
            break

def make_archers(depth, temp, cur):
    if depth == 3:
        archers_set.append(temp)
        return
    for i in range(cur, m):
        if visited[i] == False:
            visited[i] = True
            make_archers(depth+1, temp + [i], i)
            visited[i] = False
visited = [False] * m

mat_d = []
for i in range(n):
    temp = list(map(int, input().split()))
    mat_d.append(temp)


archers_set = []

for i in range(m):
    visited[i] = True
    make_archers(1, [i], i)
    visited[i] = False


# 6번째 열에 궁수가 있다고 가정
max_kill = 0
for archers in archers_set:
    mat = copy.deepcopy(mat_d)
    temp_kill = 0
    for i in range(n, 0, -1):

        tem = set()
        for archer in archers:
            find_kill(i, archer)


        # tem 돌려서 삭제 최신화
        for v1, v2 in tem:
            temp_kill += 1
            mat[v1][v2] = 0

        # 한칸 이동 후 안죽은 적 제거
        for jjj in range(m):
            mat[i-1][jjj] = 0

        # 한 칸 올리기 전 궁수 제거
    if max_kill < temp_kill:
        max_kill = temp_kill
print(max_kill)

