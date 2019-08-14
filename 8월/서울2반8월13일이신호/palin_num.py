from pprint import pprint
for tc in range(1, 11):
    n = int(input())
    matrix = []
    for _ in range(8):
        temp = list(input())
        matrix += [temp]

    result = 0
    for i in range(8):
        for j in range(9-n):
            count = 0
            for k in range(n):
                if matrix[i][j+k] == matrix[i][j+n-k-1]:
                    count += 1
            if count == n:
                result += 1

    for i in range(8):
        for j in range(8-n+1):
            count = 0
            for k in range(n):
                if matrix[j+k][i] == matrix[j+n-k-1][i]:
                    count += 1
            if count == n:
                result += 1

    print('#{} {}'.format(tc, result))

