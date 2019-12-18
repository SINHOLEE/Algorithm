import sys
input = sys.stdin.readline
def find(x):
    if root[x] == x:

        return x
    y = find(root[x])
    root[x] = y

    return y

def union(x,y):
    x = find(x)
    y = find(y)
    if root[y] == x:
        return
    root[y] = x
    network[x] = network[x] + network[y]
t = int(input())
for _ in range(t):
    n = int(input())
    name = {}
    cnt = 0
    root = []
    network = []
    for _ in range(n):
        temp = list(map(str, input().strip().split()))
        for a in temp:
            if name.get(a) == None:
                name[a] = cnt
                root.append(cnt)
                network.append(1)
                cnt += 1

        union(name[temp[0]], name[temp[1]])
        print(network[find(name[temp[0]])])
