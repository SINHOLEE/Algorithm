def DFS(depth, node1, dfs_list,visited, list_adj):
    global N, DFS_list, check
    if check:
        return
    if depth == N-1:
        DFS_list = dfs_list[:]
        check = True
        return

    for j in list_adj[node1]:
        if visited[j] == False:
            visited[j] = True
            DFS(depth+1, j, dfs_list+[j],visited, list_adj)
            visited[j] = False

N, M, start = map(int, input().split())

list_adj = [[]for _ in range(N+1)]
for m in range(M):
    i, node = map(int, input().split())
    if len(list_adj[i]) == 0:
        list_adj[i].append(node)
    else:
        list_adj[i][-1:] = [list_adj[i][-1], node]
    if len(list_adj[node]) == 0:
        list_adj[node].append(i)
    else:
        list_adj[node][-1:] = [list_adj[node][-1], i]
DFS_list = []
BFS_list = []
for _ in range(M):
    if list_adj[_]:
        list_adj[_] = sorted(list_adj[_])
print(list_adj)

visited = [False] * (N+1)
visited[start] = True
check = False
DFS(0, start, [start],visited, list_adj)
print(DFS_list)
