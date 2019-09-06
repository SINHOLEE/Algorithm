def to_do(what_to_do, index, value):
    global my_list

    if what_to_do == 'I':
        left = my_list[:index]
        right = my_list[index:]
        my_list = left + [value] + right

    elif what_to_do == 'D':
        if index == 0:
            my_list = my_list[1:]
        elif index == len(my_list) - 1:
            my_list = my_list[:-1]
        else:
            left = my_list[:index]
            right = my_list[index + 1:]
            my_list = left + right

    else:
        my_list[index] = value

T = int(input())


for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    my_list = list(map(int, input().split()))

    for num_of_trial in range(M):
        temp = list(map(str, input().split()))
        # print(temp)
        if temp[0] == 'D':
            temp[1] = int(temp[1])

            to_do(temp[0], temp[1], 0)
        else:

            temp[1] = int(temp[1])
            temp[2] = int(temp[2])
            to_do(temp[0], temp[1], temp[2])


    try:
        print('#{} {}'.format(tc, my_list[L]))
    except:
        print('#{} -1'.format(tc))