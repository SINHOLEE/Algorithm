for tc in range(1, 11):
    length, start = map(int, input().split())
    temp = list(map(int, input().split()))
    people = [[] for _ in range(101)]
    visited = [0] * 101

    for i in range(0, len(temp), 2):
        if temp[i + 1] in people[temp[i]]:
            pass
        else:
            people[temp[i]].append(temp[i + 1])


    my_queue = []
    count = 0
    visited[start] = 1
    my_queue.append(start)
    while my_queue:
        my_max = 0
        count += 1

        new = []
        for i in range(len(my_queue)):  # k값이 도는동아 range의 범위는 변하지 않는다 크.
            k = my_queue.pop(0)
            if my_max < k:
                my_max = k

            for j in range(len(people[k])):
                if visited[people[k][j]] == 0:
                    visited[people[k][j]] = 1
                    my_queue.append(people[k][j])


    print('#{} {}'.format(tc, my_max))



    #
    #
    # v = [start]
    # depth = {}
    # key_num = 0
    # my_queue = []
    # my_queue.append(v)
    # while True:
    #     node = my_queue.pop(0)
    #     new = []
    #     count = 0
    #     for nn in range(len(node)):
    #         if visited[node[nn]] == 0:
    #             visited[node[nn]] = 1
    #             for nnn in range(len(people[node[nn]])):
    #                 if visited[people[node[nn]][nnn]] == 1:
    #                     pass
    #                 else:
    #                     new.append(people[node[nn]][nnn])
    #         else:
    #             count += 1
    #     if count == len(node):
    #         break
    # #     print(new)
    #     key_num += 1
    #     depth.update({key_num : new})
    #     my_queue.append(new)
    # print('#{} {}'.format(tc, max(depth[key_num - 1])))