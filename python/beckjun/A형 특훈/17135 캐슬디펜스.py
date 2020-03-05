'''
느낌점
1. deepcopy보다 dummy_mat = [item[:] for item in mat ] 가 더 빠르다.
2. for문에 집착하지 말자.
3. 조합, 순열의 기본은 for문이다. 간단하게 짤 생각하자.
'''

from pprint import pprint
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
                if new_i + di[k] < 0 or new_i + di[k] > n-1 or new_j +dj[k] < 0 or new_j +dj[k] > m-1: # 벽이니 패스
                    pass
                elif mat[new_i+di[k]][new_j+dj[k]]:
                    tem.add((new_i+di[k], new_j+dj[k]))
                    flag = True
                    break
                new_i += di[k]
                new_j += dj[k]
            if flag:
                break
        if flag:
            break


mat_d = []
for i in range(n):
    temp = list(map(int, input().split()))
    mat_d.append(temp)


archers_set = []

# 6번째 열에 궁수가 있다고 가정
max_kill = 0

for a in range(m):
    for b in range(a+1, m):
        for c in range(b+1, m):

            mat = [row[:] for row in mat_d]
            temp_kill = 0
            for i in range(n, 0, -1):
                tem = set()
                find_kill(i, a)
                find_kill(i, b)
                find_kill(i, c)

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

