from pprint import pprint
import sys
sys.stdin = open('input_sum.txt', 'r')
sys.stdout = open('output_sum.txt', 'w', encoding='utf-8')

for tc in range(1, 11):
    case_num = int(input())
    matrix = []
    for x in range(1, 101):

        temp = list(map(int, input().split()))
        matrix += [temp]
        temp = []
        
    # matrix_t = []
    # for i in range(0, 100):
    #     a = [0] * 100
    #     matrix_t += [a]

    # for i in range(len(matrix)):
    #     for j in range(len(matrix[i])):
    #         matrix_t[i][j] = matrix[j][i]


    result = 0
    my_sum = 0
    for i in range(len(matrix)):
        # print(matrix[i][len(matrix)-1-i])
        my_sum += matrix[i][len(matrix)-1-i]
        if result < my_sum:
            result = my_sum
       
    my_sum = 0
    for i in range(len(matrix)):
        # print(matrix[i][len(matrix)-1-i])
        my_sum += matrix[i][i]
        if result < my_sum:
            result = my_sum
        

    for i in range(len(matrix)):
        my_sum = 0
        for j in range(len(matrix[i])):
            my_sum += matrix[i][j]
            if result < my_sum:
                result = my_sum
            

    for i in range(len(matrix[0])):
        my_sum = 0
        for j in range(len(matrix)):
            my_sum += matrix[j][i]
            if result < my_sum:
                result = my_sum
           

    print('#{} {}'.format(tc, result))
        
        
        
