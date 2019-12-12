from collections import deque
n,m = map(int,input().split())

visited = [0] * (n+1)
indgree = [0] * (n+1)
adj_list = [[] for _ in range(n+1)]
for _ in range(m):
    temp = [*map(int, input().split())]
    for i in range(temp[0]-1):
        adj_list[temp[1:][i]].append(temp[1:][i+1])
        indgree[temp[1:][i+1]] += 1

# 1. 진입차수가 0인 가수  큐에 넣기
dq = deque([])
for k in range(1, n+1):
    if indgree[k]:
        continue
    dq.append(k)

cnt = 0
nodes = [-1] * n
while dq:
    v = dq.popleft()
    visited[v] = 1
    nodes[cnt] = v
    cnt+=1
    for k in adj_list[v]:
        if visited[k] == 0:
            indgree[k] -= 1
            if indgree[k] == 0:
                dq.append(k)
if cnt == n:
    for node in nodes:
        print(node)
else:
    print(0)