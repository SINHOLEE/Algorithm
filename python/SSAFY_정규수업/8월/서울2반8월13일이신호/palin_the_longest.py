from pprint import pprint
from random import choice

import sys
sys.stdin = open('palin_the_longest_input.txt', 'r')
sys.stdout = open('palin_the_longest_output.txt', 'w', encoding='utf-8')



def find_the_longetst(li, max_n):
    if max_n == 0:
        for n in range(len(li), 0, -1):

            for k in range(len(li)-n+1):
                check_false = 0
                for i in range(n//2):
                    if ord(li[k+i]) - ord(li[k+n-i-1]):
                        check_false += 1
                        break
                if check_false:
                    pass
                else:
                    if max_n < n:
                        max_n = n
    else:
        for n in range(max_n, len(li)):
            for k in range(len(li) - n + 1):
                check_false = 0
                for i in range(n//2):
                    # 만약 두 아스키 코드의 차가 0이 아닐때 = 참일때,
                    if bool(ord(li[k + i]) - ord(li[k + n - i - 1])):
                        check_false += 1
                        break
                if check_false:
                    pass
                else:
                    if max_n < n:
                        max_n = n

    return max_n

for tc in range(1, 11):
    mat = [[0] * 100 for _ in range(100)]
    t = int(input())
    for i in range(100):
        temp = input()
        for j in range(len(temp)):
            mat[i][j] = temp[j]
    max_n = 0
    for i in range(len(mat)):
        max_n = find_the_longetst(mat[i], max_n)



    # 전치행렬 만들기
    mat_t = [[0] * len(mat) for _ in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat_t[i][j] = mat[j][i]

    for i in range(len(mat_t)):
        max_n = find_the_longetst(mat_t[i], max_n)
    print('#{} {}'.format(tc, max_n))

