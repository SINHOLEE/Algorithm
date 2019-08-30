T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V는 정점의 개수, E는 간선의 개수
    my_list = [[] for _ in range(V + 1)]
    for e in range(E):
        start_node, end_node = map(int, input().split())
        my_list[start_node].append(end_node)
        my_list[end_node].append(start_node)
    first_node, last_node = map(int, input().split())

    # print(my_list)
    # print(V, E)
    # print(first_node, last_node)
    visited = [0] * (V + 1)

    count = 0  # 노드의 개수
    my_queue = []
    # 첫번째 depth 진입
    my_queue.append(first_node)

    while my_queue:  # my_queue가 비워질때까지 반복


        if last_node in my_queue:
            break
        for j in range(len(my_queue)):
            node = my_queue.pop(0)
            if visited[node] == 0: #내가 방문한적이 없으면
                visited[node] = 1  # 방문한걸로 함
                for i in range(len(my_list[node])): # 내가 가지고 있는 리스트
                    if visited[my_list[node][i]] == 1:
                        pass
                    else:
                        my_queue.append(my_list[node][i])
            else:
                pass

        count += 1

    if not my_queue:
        print('#{} 0'.format(tc))
    else:
        print('#{} {}'.format(tc, count))
