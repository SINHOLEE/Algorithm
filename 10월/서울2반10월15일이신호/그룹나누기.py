T = int(input())

for tc in range(1, T+1):
    N, m = map(int, input().split())

    my_list = list(map(int, input().split()))
    list_adj = [[] for _ in range(N+1)]
    for i in range(0, len(my_list), 2):
        list_adj[my_list[i]].append(my_list[i+1])
        list_adj[my_list[i+1]].append(my_list[i])


    # print(list_adj)
    visited = [False] * (N+1)
    count = 0
    for j in range(1,N+1):
        if visited[j] == True:
            continue
        my_stack = [j]
        visited[j] = True
        temp = [j]
        while True:
            if not my_stack:
                break
            node = my_stack.pop()

            for k in list_adj[node]:
                if visited[k] == False:
                    visited[k] = True
                    my_stack.append(k)
                    temp.append(k)
        count+=1
    print('#%s %s' % (tc, count))
