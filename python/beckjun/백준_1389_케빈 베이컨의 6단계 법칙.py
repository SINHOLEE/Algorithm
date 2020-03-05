n, m = map(int, input().split())

adj_mat = [[9999999] * (n+1) for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj_mat[a][b] = 1
    adj_mat[b][a] = 1


for k in range(1, n+1):
    for i in range(1, n+1):
        if i == k:
            continue
        for j in range(1, n+1):
            if i == j:
                continue
            if adj_mat[i][k] + adj_mat[k][j] < adj_mat[i][j]:
                adj_mat[i][j] = adj_mat[i][k] + adj_mat[k][j]

min_idx = -1
min_value = 99999999
for i in range(1, n+1):
    temp = sum(filter(lambda x : x != 9999999, adj_mat[i]))
    if temp < min_value:
        min_value = temp
        min_idx = i
print(min_idx)