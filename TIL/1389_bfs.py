n, m = map(int, input().split())

adj_list = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

min_val =  999999999
min_idx = -1
for i in range(1, n+1):
    visited = [-1] * (1 + n)
    visited[i] = 1
    q = [(i, 0)]
    while q:
        idx, cnt = q.pop(0)

        for j in adj_list[idx]:
            if visited[j] == -1:
                visited[j] = cnt + 1
                q.append((j, cnt + 1))
    temp = sum(visited)
    if min_val > temp:
        min_val = temp
        min_idx = i

print(min_idx)