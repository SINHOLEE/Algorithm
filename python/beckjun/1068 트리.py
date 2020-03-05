
def tree(v):
    global cnt
    if len(node[v]) == 0:
        cnt += 1
        return

    if visited[v] == False:
        visited[v] = True
        for i in node[v]:
            if visited[i] == False:
                tree(i)

n = int(input())
temp = list(map(int, input().split()))

node = [[] for _ in range(n)]
target = int(input())
leaf = [-1] * n
for i in range(n):
    if temp[i] == -1:
        start = i
        continue
    node[temp[i]].append(i)
    leaf[i] = temp[i]
cnt = 0
visited = [False] * n

new = []
for item in node[leaf[target]]:
    if item == target:
        continue
    new.append(item)
node[leaf[target]] = new


if target != start:

    tree(start)
print(cnt)

