from pprint import pprint
cube = [
 ['*', '*', '*', 'o', 'o', 'o', '*', '*', '*', '*', '*', '*'],
 ['*', '*', '*', 'o', 'o', 'o', '*', '*', '*', '*', '*', '*'],
 ['*', '*', '*', 'o', 'o', 'o', '*', '*', '*', '*', '*', '*'],
 ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b', 'y', 'y', 'y'],
 ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b', 'y', 'y', 'y'],
 ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b', 'y', 'y', 'y'],
 ['*', '*', '*', 'r', 'r', 'r', '*', '*', '*', '*', '*', '*'],
 ['*', '*', '*', 'r', 'r', 'r', '*', '*', '*', '*', '*', '*'],
 ['*', '*', '*', 'r', 'r', 'r', '*', '*', '*', '*', '*', '*']]




# u -
#

def u_minus():
    my_queue = []
    for i in range(9):
        my_queue.append(cube[i][2])
    for j in range(9):
        my_queue.append(cube[6][j])
        cube[6][j] = my_queue.pop(0)
    for i in range(9 - 1, -1, -1):
        my_queue.append(cube[i][6])
        cube[i][6] = my_queue.pop(0)
    for j in range(9 - 1, -1, -1):
        my_queue.append(cube[2][j])
        cube[2][j] = my_queue.pop(0)
    for i in range(9):
        cube[i][2] = my_queue.pop(0)
#
    # 1
    for i in range(3, 6):
        for j in range(3, 6):
            my_queue.append(cube[i][j])
    for j in range(3, 6):
        for i in range(5, 2, -1):
            cube[i][j] = my_queue.pop(0)

# u +
def u_plus():
    my_queue = []
    for i in range(9):
        my_queue.append(cube[i][2])
        cube[i][2] = '#'
    for j in range(9-1, -1, -1):
        my_queue.append(cube[2][j])
        cube[2][j] = my_queue.pop(0)
    for i in range(9-1, -1, -1):
        my_queue.append(cube[i][6])
        cube[i][6] = my_queue.pop(0)
    for j in range(9):
        my_queue.append(cube[6][j])
        cube[6][j] = my_queue.pop(0)
    for i in range(9):
        cube[i][2] = my_queue.pop(0)

    for i in range(3, 6):
        for j in range(3, 6):
            my_queue.append(cube[i][j])
    for j in range(5, 2, -1):
        for i in range(3, 6):
            cube[i][j] = my_queue.pop(0)
# print()
# pprint(cube)

# F -
# i == 5
def f_minus():
    my_queue = []
    for j in range(12):
        my_queue.append(cube[5][j])
    for j in range(9, 12):
        cube[5][j] = my_queue.pop(0)
    for j in range(9):
        cube[5][j] = my_queue.pop(0)

    for i in range(6, 9):
        for j in range(3, 6):
            my_queue.append(cube[i][j])
    for j in range(3, 6):
        for i in range(9 - 1, 5, -1):
            cube[i][j] = my_queue.pop(0)
# pprint(cube)

# F +
# i == 5
def f_plus():
    my_queue = []
    for j in range(12):
        my_queue.append(cube[5][j])
    for j in range(3, 12):
        cube[5][j] = my_queue.pop(0)
    for j in range(3):
        cube[5][j] = my_queue.pop(0)

    for i in range(6, 9):
        for j in range(3, 6):
            my_queue.append(cube[i][j])
    for j in range(5, 2, -1):
        for i in range(6, 9):
            cube[i][j] = my_queue.pop(0)
# pprint(cube)


# B-
# i == 5
def b_minus():
    my_queue = []
    for j in range(12):
        my_queue.append(cube[3][j])
    for j in range(3, 12):
        cube[3][j] = my_queue.pop(0)
    for j in range(3):
        cube[3][j] = my_queue.pop(0)

    for i in range(0, 3):
        for j in range(3, 6):
            my_queue.append(cube[i][j])
    for j in range(3, 6):
        for i in range(2, -1, -1):
            cube[i][j] = my_queue.pop(0)
# print()
# pprint(cube)

# B+
# i == 5
def b_plus():
    my_queue = []
    for j in range(12):
        my_queue.append(cube[3][j])
    for j in range(9, 12):
        cube[3][j] = my_queue.pop(0)
    for j in range(9):
        cube[3][j] = my_queue.pop(0)

    for i in range(0, 3):
        for j in range(3, 6):
            my_queue.append(cube[i][j])
    for j in range(5, 2, -1):
        for i in range(0, 3):
            cube[i][j] = my_queue.pop(0)
# print()
# pprint(cube)
# #

#L -
def l_minus():
    my_queue = []
    for i in range(3, 6):
        for j in range(0, 3):
            my_queue.append(cube[i][j])
    for j in range(0, 3):
        for i in range(5, 2, -1):
            cube[i][j] = my_queue.pop(0)

    for i in range(9):
        my_queue.append(cube[i][3])
    for i in range(5, 2, -1):
        my_queue.append(cube[i][11])

    for i in range(5, 2, -1):
        cube[i][11] = my_queue.pop(0)
    for i in range(9):
        cube[i][3] = my_queue.pop(0)

# print()
# pprint(cube)

#L +
def l_plus():
    my_queue = []
    for i in range(3, 6):
        for j in range(0, 3):
            my_queue.append(cube[i][j])
    for j in range(2, -1, -1):
        for i in range(3, 6):
            cube[i][j] = my_queue.pop(0)

    for i in range(9):
        my_queue.append(cube[i][3])
    for i in range(5, 2, -1):
        my_queue.append(cube[i][11])

    for i in range(3, 9):
        cube[i][3] = my_queue.pop(0)
    for i in range(5, 2, -1):
        cube[i][11] = my_queue.pop(0)
    for i in range(3):
        cube[i][3] = my_queue.pop(0)

# print()
# pprint(cube)


# R -
def r_minus():
    my_queue = []
    for i in range(3, 6):
        for j in range(6, 9):
            my_queue.append(cube[i][j])
    for j in range(6, 9):
        for i in range(5, 2, -1):
            cube[i][j] = my_queue.pop(0)

    for i in range(9):
        my_queue.append(cube[i][5])
    for i in range(5, 2, -1):
        my_queue.append(cube[i][9])

    for i in range(3, 9):
        cube[i][5] = my_queue.pop(0)
    for i in range(5, 2, -1):
        cube[i][9] = my_queue.pop(0)
    for i in range(3):
        cube[i][5] = my_queue.pop(0)


# print()
# pprint(cube)

# R +
def r_plus():
    my_queue = []
    for i in range(3, 6):
        for j in range(6, 9):
            my_queue.append(cube[i][j])
    for j in range(8, 5, -1):
        for i in range(3, 6):
            cube[i][j] = my_queue.pop(0)
    #
    for i in range(9):
        my_queue.append(cube[i][5])
    for i in range(5, 2, -1):
        my_queue.append(cube[i][9])

    for i in range(5, 2, -1):
        cube[i][9] = my_queue.pop(0)
    for i in range(9):
        cube[i][5] = my_queue.pop(0)
#
# print()
# pprint(cube)

# D+
def d_plus():
    my_queue = []
    for i in range(3, 6):
        for j in range(9, 12):
            my_queue.append(cube[i][j])
    for j in range(11, 8, -1):
        for i in range(3, 6):
            cube[i][j] = my_queue.pop(0)

    for i in range(3, 6):
        my_queue.append(cube[i][8])
    for j in range(3, 6):
        my_queue.append(cube[0][j])
        cube[0][j] = my_queue.pop(0)
    for i in range(5, 2, -1):
        my_queue.append(cube[i][0])
        cube[i][0] = my_queue.pop(0)
    for j in range(5, 2, -1):
        my_queue.append(cube[8][j])
        cube[8][j] = my_queue.pop(0)
    for i in range(3, 6):
        cube[i][8] = my_queue.pop(0)

# print()
# pprint(cube)

# D-
def d_minus():
    my_queue = []
    for i in range(3, 6):
        for j in range(9, 12):
            my_queue.append(cube[i][j])
    for j in range(9, 12):
        for i in range(5, 2, -1):
            cube[i][j] = my_queue.pop(0)
    #
    for i in range(3, 6):
        my_queue.append(cube[i][8])
    for j in range(5, 2, -1):
        my_queue.append(cube[8][j])
        cube[8][j] = my_queue.pop(0)
    for i in range(5, 2, -1):
        my_queue.append(cube[i][0])
        cube[i][0] = my_queue.pop(0)
    for j in range(3, 6):
        my_queue.append(cube[0][j])
        cube[0][j] = my_queue.pop(0)
    for i in range(3, 6):
        cube[i][8] = my_queue.pop(0)
# print()
# pprint(cube)

T = int(input())
for tc in range(T):
    # cube = [
    #     ['*', '*', '*', '1', 'o', '2', '*', '*', '*', '*', '*', '*'],
    #     ['*', '*', '*', 'o', 'o', 'o', '*', '*', '*', '*', '*', '*'],
    #     ['*', '*', '*', '3', 'o', '3', '*', '*', '*', '*', '*', '*'],
    #     ['1', 'g', '3', '3', 'w', '3', '3', 'b', '2', '2', 'y', '1'],
    #     ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b', 'y', 'y', 'y'],
    #     ['7', 'g', '4', '4', 'w', '5', '5', 'b', '6', '6', 'y', '7'],
    #     ['*', '*', '*', '4', 'r', '5', '*', '*', '*', '*', '*', '*'],
    #     ['*', '*', '*', 'r', 'r', 'r', '*', '*', '*', '*', '*', '*'],
    #     ['*', '*', '*', '7', 'r', '6', '*', '*', '*', '*', '*', '*']]
    cube = [
        ['*', '*', '*', 'o', 'o', 'o', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', 'o', 'o', 'o', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', 'o', 'o', 'o', '*', '*', '*', '*', '*', '*'],
        ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b', 'y', 'y', 'y'],
        ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b', 'y', 'y', 'y'],
        ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b', 'y', 'y', 'y'],
        ['*', '*', '*', 'r', 'r', 'r', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', 'r', 'r', 'r', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', 'r', 'r', 'r', '*', '*', '*', '*', '*', '*']
    ]

    N = int(input())
    rotate = list(map(str, input().split()))
    for n in range(N):
        if rotate[n] == 'U+':
            u_plus()
        elif rotate[n] == 'U-':
            u_minus()
        elif rotate[n] == 'F+':
            f_plus()
        elif rotate[n] == 'F-':
            f_minus()
        elif rotate[n] == 'B+':
            b_plus()
        elif rotate[n] == 'B-':
            b_minus()
        elif rotate[n] == 'L+':
            l_plus()
        elif rotate[n] == 'L-':
            l_minus()
        elif rotate[n] == 'R+':
            r_plus()
        elif rotate[n] == 'R-':
            r_minus()
        elif rotate[n] == 'D+':
            d_plus()
        elif rotate[n] == 'D-':
            d_minus()
    # pprint(cube)
    for ii in range(3,6):
        for jj in range(3, 6):
            print(cube[ii][jj], end = '')
        print()




