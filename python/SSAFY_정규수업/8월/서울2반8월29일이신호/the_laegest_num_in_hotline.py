for tc in range(1, 11):
    length, start = map(int, input().split())
    temp = list(map(int, input().split()))
    people = [[] for _ in range(101)]
    visited = [0] * 101
    key_num = 0
    depth = [[] for _ in range(10)]
    max_num = 0
    for i in range(0, len(temp), 2):
        # print(i, temp[i], i + 1, temp[i + 1])
        if temp[i + 1] in people[temp[i]]:
            pass
        else:
            people[temp[i]].append(temp[i + 1])
    # print(people)


    v = [start]
    depth = {}
    key_num = 0
    my_queue = []
    my_queue.append(v)
    while True:
        node = my_queue.pop(0)
        new = []
        count = 0
        for nn in range(len(node)):
            if visited[node[nn]] == 0:
                visited[node[nn]] = 1
                for nnn in range(len(people[node[nn]])):
                    if visited[people[node[nn]][nnn]] == 1:
                        pass
                    else:
                        new.append(people[node[nn]][nnn])
            else:
                count += 1
        if count == len(node):
            break
    #     print(new)
        key_num += 1
        depth.update({key_num : new})
        my_queue.append(new)
    print('#{} {} {}'.format(tc, max(depth[key_num - 1]), key_num-1))
# data = {}
#
# data.update( {1 : [1, 2, 3]} )
# print(data)