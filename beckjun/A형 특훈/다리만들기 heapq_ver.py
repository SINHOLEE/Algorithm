'''
할말 많음
1) 제어할때는 꼭 모든 조건을 다 고려하자 ex) mat[i][j] == 0, 1, 그외 이라면, 꼭 각각의 경우를 생각해서 제어할 수 있어야 한다.
2) 나한테 부족한 할고리즘(프림, 크루스칼, 디스조인트, 다익스트라 등) 기본형 문제 2개, 응용형 문제 2개 씩 풀어본다.
3) 더 간단한 로직을 찾아본다.
'''
import heapq

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

DEBUG = True
def dfs(i, j):
    global cnt
    s = [(i, j)]
    visited[i][j] = 1
    mat[i][j] = cnt
    while s:
        x, y = s.pop()
        for k in range(4):
            xx = x+di[k]
            yy = y+dj[k]
            if 0<= xx< n and 0<= yy < m:
                if visited[xx][yy] == 0 and mat[xx][yy]==1:
                    visited[xx][yy] = 1
                    s.append((xx, yy))
                    mat[xx][yy] = cnt
def find_legs(num_of_land, x,  y, direction):
    cnt = 0
    while True:
        if mat[x][y] != 0 and mat[x][y] != num_of_land:
            if cnt >=2:
            # 만약 한 진행방향으로 가면서, 내 번호와 다른 번호의 섬과 마주치면 멈춘고
            # 그때까지의 cnt와 지금 가지고 있는 cost정보를 갱신한다.
                if DEBUG:
                    print('s, e',num_of_land, mat[xx][yy])
                adj_mat[num_of_land][mat[x][y]] = min(cnt, adj_mat[num_of_land][mat[x][y]])
            else:
                cnt = 0
            break
        xx = x+di[direction]
        yy = y+dj[direction]
        # 진행을 제어할 때, 3개의 조건이라면, 꼭 if, elif, else조건으로 제어하자.
        if 0 <= xx < n and 0 <= yy < m:
            if mat[xx][yy] == 0:
                cnt += 1
                x = xx
                y = yy
            elif mat[xx][yy] != num_of_land:
                x = xx
                y = yy
            else:
                cnt = 0
                break
            if DEBUG:
                print(x, y)
        else:
            cnt = 0
            break
    if DEBUG:
        print()
        for a in adj_mat:
            print(a)
        print(cnt)
        print()



n, m = map(int,input().split())

mat = [list(map(int,input().split())) for _ in range(n)]

# step1 섬들 구분하기
visited = [[0] * m for _ in range(n)]
cnt = 1
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and mat[i][j]==1:
            dfs(i, j)
            cnt += 1
if DEBUG:
    print('cnt', cnt)
    for a in mat:
        print(a)

# step2 다리의 모든 경우 찾기
adj_mat = []
for i in range(cnt):
    temp = [101] * (cnt)
    temp[i] = 0
    adj_mat.append(temp)

for i in range(n):
    for j in range(m):

        if mat[i][j] != 0:  # 육지 중에서
            for k in range(4): # 사방을 보는데 바다일 경우,
                ii = i + di[k]
                jj = j + dj[k]
                if 0<= ii<n and 0<= jj<m and mat[ii][jj]==0:
                    if DEBUG:
                        print('start', i,j)
                    find_legs(mat[i][j],i, j, k)



# step3 MST 구하기

keys = [[101, i, -1] for i in range(cnt)]
keys[3][0] = 0 # 스타트 노드 초기화
visited = [0] * cnt
hq = [keys[3]]

while hq:
    value, u, from_node = heapq.heappop(hq)
    keys[from_node][2] = u
    visited[u] = 1

    for v in range(1, cnt):
        if visited[v] == 0 and keys[v][0] > adj_mat[u][v]:
            #현재 방문했던 노드에서부터 진출할 수 있는 최소간선보다, 새로운 노드가 추가됨으로써
            # 더 낮은비용의 간선이 있다면 그 간선을 선택한다 or 그 간선 만? 선택한다.
                keys[v][0] = adj_mat[u][v]
                keys[v][2] = u
                heapq.heappush(hq,keys[v])
print(keys)

for key, node, f in keys:
    if node == 0:
        continue
    if key == 101:
        print(-1)
        break
else:
    print(sum(map(lambda x:x[0], keys[1:])))