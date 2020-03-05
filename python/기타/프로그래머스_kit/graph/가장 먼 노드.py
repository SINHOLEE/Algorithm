from collections import deque

def solution(n, edge):
    visited = [True] + [False] * n
    list_adj = [[] for _ in range(n+1)]
    for i in range(len(edge)):
        list_adj[edge[i][0]].append(edge[i][1])
        list_adj[edge[i][1]].append(edge[i][0])
    # print(list_adj)
    my_queue = deque()
    my_queue.extend([1])
    visited[1] = True
    depth = 1
    count = 0
    dic = {}
    dic[depth] = 1
    while True:

        depth += 1
        dic[depth] = 0

        for i in range(len(my_queue)):

            node = my_queue.popleft()
            # visited[node] = True


            for k in list_adj[node]:
                if visited[k] == False:
                    my_queue.append(k)
                    dic[depth] += 1
                    visited[k] = True
        if not my_queue:
            break
    # print(dic)
    answer = dic[max(dic)-1]
    return answer
# print(solution(n, edge))