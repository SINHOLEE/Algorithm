import heapq
import sys

# 9:50
input = sys.stdin.readline
V,e = map(int, input().split())
adj_list = [{} for _ in range(V+1)]
visited = [False] * (V+1)
distance = [V*1000000] *(V+1)
start = 1
for _ in range(e):
	u,v,w = map(int,input().split())
	if adj_list[u].get(v) is None:
		adj_list[u][v] = w
		adj_list[v][u] = w
	

# 초기화
distance[start] = 0
# 탐색
hq = []
heapq.heappush(hq, (distance[start], start))
while hq:
	w_of_u, u = heapq.heappop(hq)
	visited[u] = True
	for v, w_of_v in adj_list[u].items():
		if not visited[v] and  distance[v] > w_of_v:
			distance[v] = w_of_v
			heapq.heappush(hq, (w_of_v, v))

distance.pop(0)
print(sum(distance))

