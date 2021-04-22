import heapq
import sys

# 9:50
input = sys.stdin.readline
V,e = map(int, input().split())
start = int(input())
adj_list = [{} for _ in range(V+1)]
visited = [False] * (V+1)
distance_from_start = [V*10] *(V+1)

for _ in range(e):
	u,v,w = map(int,input().split())
	if adj_list[u].get(v) is None:
		adj_list[u][v] = w
	else:
		adj_list[u][v] = min(adj_list[u][v], w)

# 초기화
distance_from_start[start] = 0
# 탐색
hq = []
heapq.heappush(hq, (distance_from_start[start], start))
while hq:
	dist_til_u, u = heapq.heappop(hq)
	visited[u] = True
	for v, w in adj_list[u].items():
		if not visited[v] and  distance_from_start[v] >dist_til_u+w:
			distance_from_start[v] = dist_til_u+w
			heapq.heappush(hq, (dist_til_u+w, v))

distance_from_start.pop(0)
for dist in distance_from_start:
	print('INF' if dist == V*10 else dist)
