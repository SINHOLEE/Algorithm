def solution(land, P, Q):
    length = len(land)
    land = sum(land, [])
    # print(dic)
    land.sort()
    print(land)
    total = sum(land)
    answer = 999999999999999999999
    first_val = 0
    pivot = land[0]
    for height in land:
        first_val += (height-pivot) * P

    first_val = (total - (land[0] * length ** 2)) * Q
    print(first_val)
    answer = min(first_val, answer)
    for i in range(1, length ** 2):
        diff = land[i] - land[i-1]
        first_val = first_val + diff*((P * i) - Q*(length ** 2 - i))
        print(first_val)
        answer = min(first_val, answer)
    # for i in range(1, len(land_list)):
    #                 # height 차이
    #     curr_height = land_list[i][0]
    #     before_height = land_list[i-1][0]
    #     times = curr_height - before_height
    #
    #

    print(answer)
    return answer


solution([[1, 2], [2,3  ]], 3, 2)
solution([[4, 4, 3], [3, 2, 2], [2, 1, 0]], 5, 3)
