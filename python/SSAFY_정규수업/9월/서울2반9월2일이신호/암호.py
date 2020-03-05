def password(location):
    global M, current_location, my_list

    last_index = len(my_list) - 1


    if current_location + M < last_index + 1:
        left = my_list[:current_location + M]
        right = my_list[current_location + M:]
        my_list = left + [left[-1] + right[0]] + right

        current_location = current_location + M
    elif current_location + M == last_index + 1:
        left = my_list
        right_element = my_list[0]
        my_list = left + [left[-1] + right_element]
        current_location = current_location + M

    elif current_location + M > last_index + 1:
        mid = current_location + M - len(my_list)
        left = my_list[:mid]
        right = my_list[mid:]
        my_list = left + [left[-1] + right[0]] + right
        current_location = (current_location + M) % len(my_list) + 1




def ten_print(li):
    if len(li) < 11:
        s = ''
        for element in range(len(li) - 1, -1, -1):
            s += ' ' + str(li[element])
    else:
        s = ''
        for element in range(len(li) - 1, len(li) - 11, -1):
            if element == len(li):
                s += str(li[element])
            else:
                s += ' ' + str(li[element])

    return s


T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())  # N은 수열의 길이, M은 수열의 개수
    my_list = list(map(int, input().split()))

    current_location = 0
    for num_of_trial in range(K):
        password(current_location)
    print('#{}{}'.format(tc, ten_print(my_list)))

