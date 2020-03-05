from pprint import pprint

def find_min(matrix, n, sum_of_elem, N):
    global my_min
    global my_barket

    if N == n:
        # print('마지막에 sum_of_elem',sum_of_elem, n)
        if sum_of_elem < my_min:
            my_min = sum_of_elem
            # print('마지막에 my_min', my_min)
            # print()
        return

    for i in range(len(matrix[n])):
        if i in my_barket:
            pass
        else:
            if my_min < sum_of_elem:
                # print(i,n,'my_min보다 sum_of_elem이 더 크다')
                return
            else:
            # print(sum_of_elem)
                sum_of_elem += matrix[n][i]
                my_barket += [i]
                find_min(matrix, n+1, sum_of_elem, N)
                sum_of_elem -= matrix[n][i]
                my_barket.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    my_min = 1001
    result = 0
    my_barket = []
    find_min(mat, 0, result, N)

    print('#{} {}'.format(tc, my_min))

