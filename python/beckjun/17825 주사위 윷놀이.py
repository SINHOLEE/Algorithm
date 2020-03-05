dices = list(map(lambda x:int(x)-1, input().split()))

def move(horses, total_score, round ):
    global max_score
    if round == 10:
        if max_score < total_score:
            max_score = total_score
        return
    for idx in range(4):
        if round == 0:
            if idx >= 1:
                continue
        elif round == 1:
            if idx >= 2:
                continue
        elif round == 2:
            if idx >= 3:
                continue

        if horses[idx] < 32: # horse
            if board[horses[idx]][dices[round]] not in horses:
                temp =horses[idx]
                horses[idx] = board[horses[idx]][dices[round]]
                move(horses, total_score + score_board[board[temp][dices[round]]], round + 1)
                horses[idx] = temp
            else:
                if board[horses[idx]][dices[round]] == 32:
                    temp = horses[idx]
                    horses[idx] = board[horses[idx]][dices[round]]
                    move(horses, total_score + score_board[board[temp][dices[round]]], round + 1)
                    horses[idx] = temp


board = {
    0: [1, 2, 3, 4, 5],
    1: [2, 3, 4, 5, 6],
    2: [3, 4, 5, 6, 7],
    3: [4, 5, 6, 7, 8],
    4: [5, 6, 7, 8, 9],
    5: [21, 22, 23, 29, 30],
    6: [7, 8, 9, 10, 11],
    7: [8, 9, 10, 11, 12],
    8: [9, 10, 11, 12, 13],
    9: [10, 11, 12, 13, 14],
    10: [24, 25, 29, 30, 31],
    11: [12, 13, 14, 15, 16],
    12: [13, 14, 15, 16, 17],
    13: [14, 15, 16, 17, 18],
    14: [15, 16, 17, 18, 19],
    15: [26, 27, 28, 29, 30],
    16: [17, 18, 19, 20, 32],
    17: [18, 19, 20, 32, 32],
    18: [19, 20, 32, 32, 32],
    19: [20, 32, 32, 32, 32],
    20: [32, 32, 32, 32, 32],
    21: [22, 23, 29, 30, 31],
    22: [23, 29, 30, 31, 20],
    23: [29, 30, 31, 20, 32],
    24: [25, 29, 30, 31, 20],
    25: [29, 30, 31, 20, 32],
    26: [27, 28, 29, 30, 31],
    27: [28, 29, 30, 31, 20],
    28: [29, 30, 31, 20, 32],
    29: [30, 31, 20, 32, 32],
    30: [31, 20, 32, 32, 32],
    31: [20, 32, 32, 32, 32],
}
score_board = [0, 2, 4, 6, 8, 10,
          12, 14, 16, 18, 20,
          22, 24, 26, 28, 30,
          32, 34, 36, 38, 40,
          13, 16, 19, 22, 24,
          28, 27, 26, 25, 30,
          35, 0]

max_score = 0

move([0,0,0,0],0,0)
print(max_score)