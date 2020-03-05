from pprint import pprint
import copy

def game(fir, sec):
    global N, check
    old_i = copy.deepcopy(fir)
    old_j = copy.deepcopy(sec)
    new_i = copy.deepcopy(fir)
    new_j = copy.deepcopy(sec)
    while True:

        new_i += directions[direction][0]
        new_j += directions[direction][1]
        if new_i < 0 or new_j < 0 or new_i > N - 1 or new_j > N - 1:  # 2048이 되면 멈춰라가 없어 아직
            break
        if mat[new_i][new_j] == 0:
            mat[new_i][new_j] = mat[old_i][old_j]
            mat[old_i][old_j] = 0
            old_i = new_i
            old_j = new_j
            continue
        elif mat[new_i][new_j] != mat[old_i][old_j]:
            break

        elif mat[new_i][new_j] == mat[old_i][old_j]:
            if changed[new_i][new_j] == True:
                break
            else:
                changed[new_i][new_j] = True
                mat[old_i][old_j] = 0
                mat[new_i][new_j] = mat[new_i][new_j] * 2
                old_i = new_i
                old_j = new_j
                break


directions = {'up' : (-1, 0), 'down' : (1, 0), 'left' : (0, -1), 'right' : (0, 1)}
T = int(input())

for tc in range(1, T+1):
    N, direction = map(str, input().split())
    N = int(N)
    mat = []
    changed = []
    for n in range(N):
        temp = list(map(int, input().split()))
        mat.append(temp)
        temp1 = [False] * N
        changed.append(temp1)
    # up
    check = False
    if direction == 'up':
        for i in range(N):
            if check:
                break
            for j in range(N):
                first = i
                second = j
                if check:
                    break
                game(first, second)
    elif direction == 'down':
        for i in range(N - 1, -1, -1):
            if check:
                break
            for j in range(N):
                if check:
                    break
                first = i
                second = j
                game(first, second)

    elif direction == 'left':
        for i in range(N):
            if check:
                break
            for j in range(N):
                if check:
                    break
                first = j
                second = i
                game(first, second)

    elif direction == 'right':
        for i in range(N - 1, -1, -1):
            for j in range(N):
                first = j
                second = i
                game(first, second)
    print('#%s' % tc)
    for _ in range(N):
        print(' '.join(map(str, mat[_])))