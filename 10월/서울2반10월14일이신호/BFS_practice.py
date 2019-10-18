in_put = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

adj_list = [[] for _ in range(8)]
for i in range(0, len(in_put), 2):
    adj_list[in_put[i]].append(in_put[i+1])
    adj_list[in_put[i+1]].append(in_put[i])
visited = [False] * 8

my_queue = []
for i in range(1, 8):
    if visited[i] == True:
        continue
    my_queue.append(i)
    while True:
        if not my_queue:
            break
        v = my_queue.pop()
        if visited[v] == False:
            visited[v] = True
            print(v, end=' ')
            for j in adj_list[v]:
                if visited[j] == False:
                    my_queue.append(j)

# print(adj_list)