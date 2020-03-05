from collections import deque
n,m = map(int, input().split())

indegree = [0] * (n+1)
adj_list = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    indegree[b] += 1


dq = deque([])
for i in range(1, n+1):
    if indegree[i] == 0:
        dq.append(i)
s = [0] * (n+1)
cnt = 1
while dq:
    node = dq.popleft()
    
    s[cnt] = node
    cnt+=1
    for k in adj_list[node]:
        indegree[k] -= 1
        if indegree[k] == 0:
            dq.append(k)
print(' '.join(map(str,s[1:])))

