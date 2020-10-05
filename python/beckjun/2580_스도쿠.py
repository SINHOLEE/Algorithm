mat = [list(map(int, input().split())) for i in range(9)]

group_board = [[0] * 9 for _ in range(9)]
group_board_pair = [[] for _ in range(9)]
temp = 0
for i in range(9):
    if i != 0 and i % 3 == 0:
        temp += 3
    cnt = 0
    for j in range(9):
        if j != 0 and j % 3 == 0:
            cnt += 1
        group_board[i][j] = temp + cnt
        group_board_pair[temp+cnt].append((i,j))

for a in group_board:
    print(a)
def check():
    return
# def col(i, j, x):
#1. 이중포문을 돌면서 0을 만나면, 3개의 확인함수를 실행한다.
#2. 세개의 실행함수는, y,x좌표를 기준으로 row, col, 해당 그리드번호의 리스트를 순회하면서 한번도 겹치는 숫자가 있는지 확인한다.
def dfs(y, x):
    # 1 가로
    for j in range(x, 9):
        if mat[y][j] == 0:
           dfs(y, j)
    for i in range(y+1, 9):
        for j in range(9):
            if mat[i][j] == 0:
                dfs(i, j)


dfs(0, 0)


print(81*9*81)