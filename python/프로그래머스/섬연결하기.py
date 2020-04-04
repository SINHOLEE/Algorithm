import math
import heapq


def solution(n, costs):
    mat = [[math.inf] * n for _ in range(n)]

    for a, b, c in costs:
        mat[a][b] = c
        mat[b][a] = c
    distance = [math.inf] * n
    distance[n-1] = 0
    visited = [0] * n
    hq = [(0, n-1)]
    cnt = 0
    res = 0
    while hq:

        cc, node = heapq.heappop(hq)
        visited[node] = 1
        for next_idx in range(n):
            if mat[node][next_idx] == math.inf:
                continue
            if visited[next_idx]:
                continue
            if mat[node][next_idx] < distance[next_idx]:
                distance[next_idx] = mat[node][next_idx]
                heapq.heappush(hq, (distance[next_idx], next_idx))
    return sum(distance)
