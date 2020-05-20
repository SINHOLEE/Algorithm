'''
mst 필수 개념
1. 노드의 개수 -1 번 반복만 해야한다.
2. 노드가 많다면,adj/-list, 간선이 많다면 adj_mat 쓰자.



'''

import heapq

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def bfs(cnt, y, x, mat, height, land_len, land):
    q = [(y,x,cnt)]
    mat[y][x] = cnt
    while q:
        y, x, cnt = q.pop(0)
        for k in range(4):
            ny, nx = y+dy[k], x+dx[k]
            if not(0<=ny<land_len and 0<= nx<land_len):
                continue
            if mat[ny][nx]:
                continue
            if abs(land[y][x] - land[ny][nx]) <= height:
                mat[ny][nx] = cnt
                q.append((ny, nx, cnt))
    return mat


def solution(land, height):
    answer = 0
    land_len = len(land)
    mat = [[0] * land_len for _ in range(land_len)]
    cnt = 0
    # 1 bfs로 구획을 나눈다.
    for i in range(land_len):
        for j in range(land_len):
            if mat[i][j]:
                continue
            cnt += 1
            mat = bfs(cnt, i, j, mat, height, land_len, land)

    # 2 adj_mat로 각 노드와 노드의 거리가 가장 작은 애들만 남긴다.
    adj_list = {}
    for i in range(land_len):
        for j in range(land_len):
            for k in range(4):
                ni, nj = i+dy[k], j+dx[k]
                if not (0 <= ni < land_len and 0 <= nj < land_len):
                    continue
                if mat[i][j] == mat[ni][nj]:
                    continue
                a = mat[i][j]
                b = mat[ni][nj]
                if adj_list.get(a) is None:
                    adj_list[a] = {}
                    if adj_list[a].get(b) is None:
                        adj_list[a][b] = abs(land[i][j] - land[ni][nj])
                    else:
                        adj_list[a][b] = min(abs(land[i][j]-land[ni][nj]), adj_list[a][b])
                else:
                    if adj_list[a].get(b) is None:
                        adj_list[a][b] = abs(land[i][j]-land[ni][nj])
                    else:
                        adj_list[a][b] = min(abs(land[i][j]-land[ni][nj]), adj_list[a][b])

    # 3 MST로 문제를 푼다.
    visited = [False] * (cnt+1)
    mst_table = [876543] * (cnt+1)
    mst_table[cnt] = 0
    temp = 0
    hq = [(0, cnt)]
    while hq:
        value, node = heapq.heappop(hq)
        visited[node] = True
        if temp == cnt - 1:
            break
        for nxt, nxt_value in adj_list[node].items():
            if mst_table[nxt] < nxt_value:
                continue
            if visited[nxt]:
                continue
            mst_table[nxt] = adj_list[node][nxt]
            heapq.heappush(hq, (adj_list[node][nxt], nxt))
    temp += 1
    # print(mst_table)
    return sum(mst_table[1:])


# print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
print(solution(	[[1, 1], [1, 1]], 1))