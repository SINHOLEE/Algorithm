from pprint import pprint
T = int(input())



for t in range(1, T+1):
    matrix = []
    for i in range(0, 10):
        a = [0] * 10
        matrix += [a]
    pprint(matrix)
    N = int(input())
    for n in range(N):
        x1, y1, x2, y2, color = input().split()
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        color = int(color)
        for col in range(y1, y2 + 1):
            for row in range(x1, x2 + 1):
                if matrix[col][row] == 0:
                    matrix[col][row] += color
                else:
                    if matrix[col][row] == color:
                        pass
                    else:
                        matrix[col][row] += color
    pprint(matrix)
    count = 0
    for x in matrix:
        for y in x:
            if y == 3:  # 3은 보라색
                count += 1
    print('#{} {}'.format(t, count))
