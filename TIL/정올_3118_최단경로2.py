import heapq
import sys
import math
input = sys.stdin.readline

n,m = map(int,input().strip().split())

dic = [{} for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())

    dic[a].update({b:c})
# visited = [0] * (n+1)
key = [math.inf for i in range(n+1)]

key[1] = 0
hq = [(key[1], 1)]
while hq:
    dis, node = heapq.heappop(hq)
    if key[node] < dis:
        continue
    if node == n:
        break
    for next in dic[node].keys():
        # if visited[next] == 0:
        now = key[next]
        compare = dis + dic[node][next]
        if now > compare:
            key[next] = compare
            heapq.heappush(hq, (compare, next))
print(key[n])