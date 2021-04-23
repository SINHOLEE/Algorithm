import heapq

def solution(N,M,mat):
    keys = [[1001, -1] for _ in range(N+1)] # cost, from
    visited = [0] * (N+1)
    keys[1] = [0,1]
    keys[0] = [0,0]
    adj_dict = {}
    for a,b,c in mat:
        if a not in adj_dict:
            adj_dict[a] = {}
            adj_dict[a][b] = c
        else:
            adj_dict[a][b] = c
        if b not in adj_dict:
            adj_dict[b] = {}
            adj_dict[b][a] = c
        else:
            adj_dict[b][a] = c
    hq = []
    heapq.heappush(hq,[0,1])
    while hq:
        _, node = heapq.heappop(hq)
        if visited[node]: continue
        visited[node] = 1
        for v, w in adj_dict[node].items():
            if visited[v]:continue
            if keys[v][0] >w:
                keys[v] = [w ,node]
                heapq.heappush(hq, [w, v])


    return sum(map(lambda x:x[0], keys)) - max(map(lambda x:x[0], keys))


if __name__ == '__main__':
    N,M = map(int, input().split(" "))
    mat = [[*map(int, input().split(" "))] for _ in range(M)]
    
    print(solution(N,M, mat))