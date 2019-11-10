import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = list(range(0,n+1))
rank = [0] * (n+1)

def find(x):
    if parent[x] == x:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y

def union(x, y):
    x = find(x)
    y = find(y)
    # 싸이클일경우 탈출
    if x == y:
        return
    if range(x) == range(y):
        parent[y] = x
        rank[x] += 1
    else:
        if rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[y] = x

for _ in range(m):
    num, a, b = map(int, input().split())
    if num == 1:
        if find(a)== find(b):
            print('YES')
        else:
            print('NO')

    else:
        union(a, b)
