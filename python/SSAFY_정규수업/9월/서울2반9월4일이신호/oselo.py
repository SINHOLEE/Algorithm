from pprint import pprint
def iswall(i, j):
    if i < 0 or j < 0 or i > len(board) - 1 or j > len(board) - 1:
        return True
    else:
        return False

def change_stone(i, j, color, board):
        #상 상우 우 우하 하 하좌 좌 좌상
    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]
    for _ in range(8):

        i = i + di[_]
        j = j + dj[_]
        if iswall(i, j) or board[i][j] == 0 or board[i][j] == color:
            i -= di[_]
            j -= dj[_]
            continue
        if color == 1:
            cnt = 0
            while True:
                i += di[_]
                j += dj[_]
                cnt += 1
                if iswall(i, j) or board[i][j] == 0:
                    for back in range(cnt):
                        i -= di[_]
                        j -= dj[_]
                    break
                if board[i][j] == color:
                    for back in range(cnt):
                        i -= di[_]
                        j -= dj[_]
                        if board[i][j] == 2:
                            board[i][j] = color
                    break
            i -= di[_]
            j -= dj[_]
        elif color == 2:
            cnt = 0
            while True:
                i += di[_]
                j += dj[_]
                cnt += 1
                if iswall(i, j) or board[i][j] == 0:
                    for back in range(cnt):
                        i -= di[_]
                        j -= dj[_]
                    break
                if board[i][j] == color:
                    for back in range(cnt):
                        i -= di[_]
                        j -= dj[_]
                        if board[i][j] == 1:
                            board[i][j] = color
                    break
            i -= di[_]
            j -= dj[_]

    return board

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    board = []
    for _ in range(N):
        temp = [0] * N
        board.append(temp)

    for i in range(N):
        if i == N // 2 - 1:
            for j in range(N):
                if j == N // 2 - 1:
                    board[i][j] = 2
                elif j == N // 2:
                    board[i][j] = 1
        elif i == N // 2:
            for j in range(N):
                if j == N // 2 - 1:
                    board[i][j] = 1
                elif j == N // 2:
                    board[i][j] = 2

    for n in range(M):
        jj, ii, color = map(int, input().split())
        i = ii - 1
        j = jj - 1
        board[i][j] = color
        board = change_stone(i, j, color, board)
        # print(n + 1)
        # pprint(board)
        # print()

    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print('#%s %d %d' % (tc, black, white))