'''
 대각선 바라보는 방법: x, y 기준으로 우 하향 대각선은, x-y와 같은 모든 값의 좌표들,
 좌 하향 대각선은 x+y의 값을 갖는 모든 좌표들
'''

from pprint import pprint
import copy
n = int(input())

population = [list(map(int, input().split())) for _ in range(n)]

dummy_mat = [[0] * n for _ in range(n) ]
total = 0
for _ in range(n):
    for __ in range(n):
        total += population[_][__]


total_min = 2001
for ii in range(0, n-2):
    for jj in range(1, n-1):
        set_d1 = range(1, jj+1)
        set_d2 = range(1, n-jj)

        for d1 in set_d1:
            for d2 in set_d2:
                if ii + d1+ d2 > n-1:
                    continue
                mat = [arr[:] for arr in dummy_mat]
                mat[ii][jj] = 4
                groups = [0, 0, 0, 0, 0]

                for a in range(1, d1+1):
                    mat[ii+a][jj-a] = 4
                    mat[ii+d2+a][jj+d2-a] = 4
                for b in range(1, d2+1):
                    mat[ii+d1+b][jj-d1+b] = 4
                    mat[ii+b][jj+b] = 4

                for i in range(ii+d1):
                    for j in range(jj+1):
                        if mat[i][j] == 4:
                            break
                        groups[0] += population[i][j]
                for i in range(ii+d2+1):
                    for j in range(n-1, jj, -1):
                        if mat[i][j] == 4:
                            break
                        groups[1] += population[i][j]
                for i in range(ii+d1,n):
                    for j in range(jj-d1+d2):
                        if mat[i][j] == 4:
                            break
                        groups[2] += population[i][j]
                for i in range(ii+d2+1, n):
                    for j in range(n-1, jj-d1+d2-1, -1):
                        if mat[i][j] == 4:
                            break
                        groups[3] += population[i][j]
                groups[4] = total - sum(groups)

                temp = max(groups) - min(groups)
                if total_min > temp:
                    total_min = temp
print(total_min)

