'''
4 3
4 3
'''
from pprint import pprint

n,m = map(int,input().split())
x, y = map(int, input().split())

if x > n or y > m:
    print('fail')
else:
    mat = []
    for i in range(y+1):
        if i == 0:
            temp = [0] + [1] * x
        else:
            temp = [1] + [0] * x
        mat.append(temp)

    for i in range(1, y+1):
        for j in range(1, x+1):

            mat[i][j] = mat[i-1][j] + mat[i][j-1]

    print(x + y)
    if (x ,y) == (0, 0):
        print('1')
    else:
        print(mat[y][x])

