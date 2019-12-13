import sys
input = sys.stdin.readline
from collections import deque

k = int(input())

for i in range(k):
    v,e = map(int, input().split())
    adj_list = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)
    set_list = [[0]*(v+1),[0]*(v+1)]
    visited = [0] *(v+1)
    flag = True
    dq = deque([])
    for i in range(1, v+1):
        if flag == False:
            break
        if visited[i] == 0:
            dq.append((0, i))
            visited[i] = 1
            set_list[0][i] = 1
            while dq:
                cnt, node = dq.popleft()
                for end_node in adj_list[node]:
                    if set_list[cnt % 2][end_node] == 1:
                        flag = False
                        break

                    if visited[end_node] == 0:
                        visited[end_node] = 1
                        set_list[(cnt+1)%2][end_node] = 1
                        dq.append((cnt+1, end_node))

                if flag == False:
                    break
    if flag:
        print('YES')
    else:
        print('NO')


