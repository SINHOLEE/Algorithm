def my_max(my_list):
    my_max_tuple = (-1, -1)

    for i in range(len(my_list)):
        if my_max_tuple[1] < my_list[i][1]:
            my_max_tuple = my_list[i]

    return my_max_tuple


def solution(priorities, location):
    my_queue = []
    answer = 0
    for i in range(len(priorities)):
        my_queue.append((i , priorities[i]))

    count = 0
    while True:
        currunt = my_queue.pop(0)
        if currunt[1] >= my_max(my_queue)[1]:
            count += 1
            if currunt[0] == location:
                answer = count
                break
        else:
            my_queue.append(currunt)

    return answer
#
