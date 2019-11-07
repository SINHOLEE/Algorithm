'''
비효율이 생긴 이유
1. 한 물고기를 먹기 위해 bfs를 매번 실행하였다. ( 효율적인 코드는 한 bfs 안에서 다 끝난다.)
2. 이렇게 설계한 이유는, 물고기의 크기가 작은! 아이들만 보려고 했기 때문이다. 이렇게 제한하여 바라보니 매번 for문을 돌게 되고 이는 매 for문이 방문할때마다 bfs를 호출하는 불상사가 일어나게 되었다.
3. 애초에 재귀를 이용한 dfs로 설계했던 코드를 bfs로 바꾸려 하다보니 꼬인것이라고 생각한다.
'''

import heapq
from collections import deque
from pprint import pprint
n = int(input())

mat = [list(map(int, input().split())) for _ in range(n)]
visited_dummy = [[False] * n for _ in range(n)]

locations = [{} for _ in range(7)]

for i in range(n):
    for j in range(n):
        if mat[i][j]:
            if mat[i][j] == 9:
                mat[i][j] = 0
                shark = [i, j, 2, 0]

    # 좌 우 상 하
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def find(x, y, goal_x, goal_y):
    global temp_dis
    hq = []
    distance_to_goal = abs(x - goal_x) + abs(y - goal_y)
    heapq.heappush(hq, [distance_to_goal, x, y, 0])
    check = False
    res = 0
    while True:
        if len(hq)==0:
            check = True
            break
        length = len(hq)
        my_data = heapq.heappop(hq)
        distance_to_goal = my_data[0]
        x = my_data[1]
        y = my_data[2]
        footstep = my_data[3]
        if x == goal_x and y == goal_y:
            res = footstep
            break
        for k in range(4):
            if x + di[k] >= 0 and x + di[k] < n and y + dj[k] >= 0 and y + dj[k] < n and visited[x + di[k]][y + dj[k]] == False and mat[x + di[k]][y + dj[k]] <= shark[2]:
                visited[x+di[k]][y+dj[k]] = True
                heapq.heappush(hq, [abs(x+di[k] - goal_x) + abs(y+dj[k] - goal_y), x+di[k], y+dj[k], footstep + 1])
    if check:
        return
    else:
        temp_dis = res
        return

total = 0
while True:
    now_data = []
    for i in range(1, 7):
        if i < shark[2]:
            temp_dis = 999999999
            for key, val in locations[i].items():
                x, y = key[0], key[1]
                visited = [arr[:] for arr in visited_dummy]
                find(shark[0], shark[1], x, y)
                heapq.heappush(now_data, [temp_dis, x, y, val])
                now_data = [heapq.heappop(now_data)]
    if len(now_data) == 0 or now_data[0][0] == 999999999:
        break
    else:
        # 먹는다.
        now_data = heapq.heappop(now_data)
        total += now_data[0]
        shark[0] = now_data[1]
        shark[1] = now_data[2]
        shark[3] += 1
        del(locations[now_data[3]][(shark[0], shark[1])])
        mat[shark[0]][shark[1]] = 0
        if shark[2] == shark[3]:
            shark[3] = 0
            shark[2] += 1
print(total)
