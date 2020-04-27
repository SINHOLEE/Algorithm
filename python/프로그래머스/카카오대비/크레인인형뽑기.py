def check():
    global stack, answer
    if len(stack) < 2:
        return
    if stack[-1] == stack[-2]:
        stack.pop()
        stack.pop()
        answer += 2
        return


def find_bottom(w_idx):
    global height, width, mat
    for i in range(height):
        if mat[i][w_idx]:
            temp = mat[i][w_idx]
            mat[i][w_idx] = 0
            return i, temp
    else:
        return -1, -1


def solution(board, moves):
    global height, width, mat, stack, answer
    mat = board
    height = len(board)
    width = len(board[0])
    for pic in moves:
        w_idx = pic - 1
        h_idx, value = find_bottom(w_idx)
        if h_idx > -1:
            stack.append(value)
        check()
    return answer


answer = 0
stack = []
mat = []
height = 0
width = 0
solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
         [1, 5, 3, 5, 1, 2, 1, 4])
