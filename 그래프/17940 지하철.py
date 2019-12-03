import heapq
import sys
input = sys.stdin.readline

n, goal = map(int,input().split())
DEBUG = False
visited = [0] * n
key = [[0,99999,i] for i in range(n)]
company = [0] * n
for _ in range(n):
    j = int(input())
    if j:
        company[_] = 1

adj_mat = [list(map(int, input().strip().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if adj_mat[i][j] == 0:
            adj_mat[i][j] = 99999

key[0] = [0,0,0]
hq = [[0,0,0]]
while hq:
    change_train, cost, node = heapq.heappop(hq)
    if node == goal:
        break
    visited[node] = 1
    if DEBUG:
        print()
        print(key)
        print('visited',visited)
        print('company', company)
        print('hq', hq)
    for v in range(n):
        if visited[v] == 0 and adj_mat[node][v] != 99999:
            if cost + adj_mat[node][v] < key[v][1]:
                key[v][1] = cost+adj_mat[node][v]
                if company[node] != company[v]:
                    key[v][0] = change_train+1
                    heapq.heappush(hq, [key[v][0], key[v][1], key[v][2]])
                else:
                    key[v][0] = change_train
                    heapq.heappush(hq, [key[v][0], key[v][1], key[v][2]])
if DEBUG:
    for a in key:
        print(a)
print('%s %s' % (key[goal][0], key[goal][1]))