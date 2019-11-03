'''
1. 무조건 나눗셈이 있는 로직은 분모가 0인지 항상 체크하기
2. 인덱싱은 항상 유의
3. 시뮬레이션 문제에서는 한 턴, 한 단계의 상태를 매 번 새로운 리스트, 혹은 튜플로 관리하고 한 단계가 넘어가면 기존 데이터와 교체하는 방식을 사용한다.
'''

from pprint import pprint

def rotate(x, d, k):
    for i in range(1, n+1):
        if i % x == 0:
            if d: # 시계방향
                left = mat[i-1][:k]
                right = mat[i-1][k:]
            else:
                left = mat[i-1][:m-k]
                right = mat[i-1][m-k:]
            mat[i-1] = right + left
    # 좌 우 상 하
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
n, m, t = map(int, input().split())

mat = []
for _ in range(n):
    temp = list(map(int, input().split()))
    mat.append(temp)

for q in range(t):
    x, d, k = map(int, input().split())
    rotate(x, d, k)
    dummy_mat = [[] for _ in range(n)]
    flag = False  # 바뀌는게 하나도 없으면 False
    count = 0 # 숫자가 0 이상
    res = 0

    for i in range(n):
        for j in range(m):
            currnt = mat[i][j]  # 이 때의 값
            if currnt == 0: # 이미 바뀌어 있다면 안봐도 됨
                dummy_mat[i].append(0)
                continue

            for k in range(4):
                if i+di[k] < 0 or i+di[k] > n - 1:
                    continue
                elif j +dj[k] <0:
                    if currnt == mat[i+di[k]][-1]:
                        dummy_mat[i].append(0)
                        flag = True
                        break
                elif j +dj[k] > m-1:
                    if currnt == mat[i+di[k]][0]:
                        dummy_mat[i].append(0)
                        flag = True
                        break
                else:
                    if currnt == mat[i+di[k]][j+dj[k]]:
                        dummy_mat[i].append(0)
                        flag = True
                        break
            else:
                dummy_mat[i].append(currnt)
                count += 1
                res += currnt

    mat = dummy_mat

    if flag == False:
        if count == 0:
            break
        avgg = res / count
        res = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    continue
                if mat[i][j] > avgg:
                    mat[i][j] = mat[i][j] - 1

                elif mat[i][j] < avgg:
                    mat[i][j] = mat[i][j] + 1
                res += mat[i][j]


print(res)


