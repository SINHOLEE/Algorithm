from pprint import pprint
import copy
nums ={"A":0, "B":1, "C":2, "D":3, "E":4,"F":5,"G":6, "H":7}
def solution(bishops):
    mat = [[0] *8  for _ in range(8)]
    points = []
    for bishop in bishops:
        points.append((nums[bishop[0]], int(bishop[1])-1))
        mat[nums[bishop[0]]][int(bishop[1])-1] = 1

    for i, j in points:
        ii = copy.deepcopy(i)
        jj = copy.deepcopy(j)
        while True: #좌상
            ii = ii -1
            jj = jj - 1
            if ii<0 or jj<0 or ii>7 or jj > 7:
                break
            mat[ii][jj] = 1
        ii = copy.deepcopy(i)
        jj = copy.deepcopy(j)

        while True:  # 좌상
            ii = ii + 1
            jj = jj + 1
            if ii < 0 or jj < 0 or ii > 7 or jj > 7:
                break
            mat[ii][jj] = 1
        ii = copy.deepcopy(i)
        jj = copy.deepcopy(j)

        while True:  # 좌상
            ii = ii + 1
            jj = jj - 1
            if ii < 0 or jj < 0 or ii > 7 or jj > 7:
                break
            mat[ii][jj] = 1
        ii = copy.deepcopy(i)
        jj = copy.deepcopy(j)

        while True:  # 좌상
            ii = ii - 1
            jj = jj + 1
            if ii < 0 or jj < 0 or ii > 7 or jj > 7:
                break
            mat[ii][jj] = 1

            answer = 0
    for i in range(8):
        for j in range(8):
            if mat[i][j]:
                continue
            answer += 1


    return answer

print(solution(bishops))