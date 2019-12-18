import heapq
import math

n,m = map(int,input().strip().split())

dic = [{} for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    dic[a][b] = c
visited = [0] * (n+1)
key = [[math.inf, i] for i in range(n+1)]

hq = [key[1]]
key[1][0] = 0
while hq:
    dis, node = heapq.heappop(hq)
    visited[node] = 1
    if node == n:
        break
    for next, distance in dic[node].items():
        if visited[next] == 0:
            if key[next][0] > dis + distance:
                key[next][0] = dis + distance
                heapq.heappush(hq, key[next])
print(key[n][0])