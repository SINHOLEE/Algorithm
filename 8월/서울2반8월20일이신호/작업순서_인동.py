# import sys
# from pprint import pprint
# sys.stdin = open("input.txt", "r")
# sys.stdout = open('output.txt', 'w', encoding='utf-8')


for case in range(1, 11):
    V, E = map(int, input().split())
    vis = [None] + [0] * V
    adj = [[] for i in range(V + 1)]
    graph = list(map(int, input().split()))

    for i in range(0, len(graph) - 1, 2):
        adj[graph[i]].append(graph[i + 1])
        vis[graph[i + 1]] += 1
    print(vis)
    path = ''
    for i in range(len(vis)):
        if vis[i] != 0:
            continue
        stack = []
        stack.append(i)
        while stack:
            node = stack.pop()
            if vis[node] > 0:
                vis[node] -= 1
            if vis[node] == 0:
                path += str(node) + ' '
                vis[node] = 'Fin'
                stack.extend(adj[node])

    print('#{} {}'.format(case, path ))
