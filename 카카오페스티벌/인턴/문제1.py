board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [0,2,4,4,2],
         [0,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
def solution(board, moves):
    bucket = []
    cnt = 0
    for move in moves:
        move -= 1
        for i in range(len(board)):
            if board[i][move]:
                bucket.append(board[i][move])
                board[i][move]=0
                break

        if len(bucket) >= 2:
            if bucket[-1] == bucket[-2]:
                cnt+=2
                bucket.pop()
                bucket.pop()

    return cnt

print(solution(board, moves))