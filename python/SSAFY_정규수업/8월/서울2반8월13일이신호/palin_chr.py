from pprint import pprint
import sys
sys.stdin = open('palin_chr_input.txt', 'r')
sys.stdout = open('palin_chr_output.txt', 'w', encoding='utf-8')

def palin(matrix, N, M):
    result = ''
    for i in range(N):
        for j in range(N-M+1):
            count = 0
            temp = []
            for k in range(M):
                if matrix[i][j+k] == matrix[i][j+M-1-k]:
                    count += 1
                    temp += [matrix[i][j+k]]
            if count == M:
                result = ''.join(map(str, temp))
                return result
                break

    matrix_t = []
    for i in range(N):
        new = [0] * N
        matrix_t += [new]
    for i in range(N):
        for j in range(N):
            matrix_t[i][j] = matrix[j][i]
    for i in range(N):
        for j in range(N-M+1):
            count = 0
            temp = []
            for k in range(M):
                if matrix_t[i][j+k] == matrix_t[i][j+M-1-k]:
                    count += 1
                    temp += [matrix_t[i][j+k]]
            if count == M:
                result = ''.join(map(str, temp))
                return result

T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    N, M = int(N), int(M)

    # make a matrix
    matrix = []
    for n in range(N):
        temp1 = list(input())
        matrix += [temp1]

    print('#{} {}'.format(tc, palin(matrix, N, M)))
