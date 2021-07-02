#pm6:17 -> 55
n, m = map(int, input().split())
keys = [i for i in range(n + 1)]
rank = [0 for i in range(n + 1)]

def find(x):
    if keys[x] == x:
        return x
    y = find(keys[x])
    keys[x] = y
    
    return y


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] == rank[y]:
        rank[x] += 1
        keys[y] = x
    elif rank[x] < rank[y]:
        keys[x] = y
    else:
        keys[y] = x
        

for _ in range(m):
    operator, a, b = map(int, input().split())
    if operator:
        print('YES' if find(a) == find(b) else 'NO')
    else:
        union(a, b)

