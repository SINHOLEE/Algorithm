N, M, start = map(int, input().split())

list_adj = [[] for H in range(N + 1)]
for m in range(M):
    i, node = map(int, input().split())
    list_adj[i].append(node)
    list_adj[node].append(i)
for k in range(1,N+1):
    if list_adj[k]:
        list_adj[k] = sorted(list_adj[k])

BFS_list = []
my_queue = []
count1 = 0
my_queue.append(start)
visited1 = [False] * (N + 1)
while True:
    count1+=1
    if not my_queue:
        break

    for _ in range(len(my_queue)):
        node2 = my_queue.pop(0)
        if visited1[node2] == False and node2 not in BFS_list:
            visited1[node2] = True
            BFS_list.append(node2)
            if list_adj[node2]:
                my_queue.extend(list_adj[node2])

DFS_list = []
my_stack = []

my_stack.append(start)
visited = [False] * (N + 1)
count2 = 0
while True:
    count2+=1
    if not my_stack:
        break
    v = my_stack.pop()
    visited[v] = True
    if v not in DFS_list:
        DFS_list.append(v)
    for node in range(len(list_adj[v]) - 1, -1, -1):
        if visited[list_adj[v][node]] == False and list_adj[v][node] not in DFS_list:
            my_stack.append(list_adj[v][node])

print('DSF 횟수',count1,':',' '.join(map(str, DFS_list)))

print('BFS 횟수',count2,':',' '.join(map(str, BFS_list)))