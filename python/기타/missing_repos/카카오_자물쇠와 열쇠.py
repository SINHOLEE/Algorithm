key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def turn(board, m):
    dummy_board = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            dummy_board[m-j-1][i] = board[i][j]
    return dummy_board


def merge_and_check(sx, sy, ex, ey, d_key, d_lock, key_len, lock_len):
    flag = False
    for i in range(sx, ex):
        for j in range(sy, ey):
            if not d_lock[i][j]:
                if d_key[i-sx][j-sy]:
                    d_lock[i][j] = 1
            else:
                if d_key[i-sx][j-sy]:
                    flag = True
                    break

    if not flag:
        flag2 = False
        for i in range(key_len-1, key_len-1+lock_len):
            for j in range(key_len - 1, key_len - 1 + lock_len):
                if not d_lock[i][j]:
                    flag2 = True
        if not flag2:
            return True
    return False

def solution(key, lock):

    key_len = len(key)
    lock_len = len(lock)
    n = key_len * 2 + lock_len - 2

    mat = [[0] * n for _ in range(n)]

    for i in range(lock_len):
        for j in range(lock_len):
            mat[key_len-1+i][key_len-1+j] = lock[i][j]
    goal = False
    # search
    for i in range(n-key_len+1):
        for j in range(n-key_len+1):
            d_key = [arr[:] for arr in key]
            for _ in range(4):
                dummy_mat = [arr[:] for arr in mat]
                goal = merge_and_check(i, j, i+key_len, j+key_len, d_key, dummy_mat, key_len, lock_len)
                if goal:
                    return goal
                d_key = turn(d_key, key_len)

    return goal

print(solution(key, lock))