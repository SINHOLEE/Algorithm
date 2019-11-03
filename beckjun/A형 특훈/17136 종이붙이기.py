'''
느낀점
1. 브레이크 포인트를 잘 생각하자. 이번경우엔 1인 애가 없을때 멈추는 것이 관건
2. 재귀는 항상 기본은 완전탐색 그 후 백트레킹으러 시간단축하기                     #
'''

def isSqure(i, j, n, local_mat):
    if i+n > 10 or j + n > 10:
        return False
    for ii in range(i, i+n):
        for jj in range(j, j+n):
            if local_mat[ii][jj] != 1:
                return False
    return True

def check(x, y, paper, cnt, mat, totalOne):
    global min_cnt
    if min_cnt < cnt:
        return
    if totalOne  == 0:
        if min_cnt > cnt:
            min_cnt = cnt
    for i in range(x, 10):
        for j in range(10):
            if i == x and j < y:
                continue


            if mat[i][j] == 1:
                for n in range(5, 0, -1):
                    if paper[n] == 0:
                        return
                    if isSqure(i, j, n, mat):

                        for ii in range(i, i+n):
                            for jj in range(j, j+n):
                                mat[ii][jj] = n+1

                        paper[n] -= 1
                        check(i, j, paper, cnt+1, mat, totalOne -(n ** 2))
                        paper[n] += 1

                        for ii in range(i, i+n):
                            for jj in range(j, j+n):
                                mat[ii][jj] = 1

                return

min_cnt = 26
board = [list(map(int, input().split())) for _ in range(10)]
total_one = sum(sum(item) for item in board)

paper_list = [0, 5, 5, 5, 5, 5]
check(0, 0, paper_list, 0, board, total_one )

if min_cnt == 26:
    print(-1)
else:
    print(min_cnt)






