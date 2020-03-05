n = int(input())
m = int(input())

adj_mat = [list(map(int, input().split()))for _ in range(n)]

route = set(map(lambda x:int(x)-1, input().split()))


visited = [False]* n

dic = {}
set_number = 1

def bfs(v):
    global set_number
    if visited[v] == True:
        return
    queue = [v]
    while queue:
        length = len(queue)
        for _ in range(length):
            v = queue.pop(0)
            if visited[v] == False:

                if dic.get(set_number) == None:
                    dic[set_number] = set([v])
                else:
                    dic[set_number].add(v)
                visited[v] = True
                for k in range(n):  #
                    if adj_mat[v][k] == 1 and visited[k] == False:
                        queue.append(k)
    set_number += 1



for i in range(n):
    bfs(i)
check = False
for k, item in dic.items():
    if route.issubset(item):
        check = True
        break
if check:
    print('YES')
else:
    print('NO')
