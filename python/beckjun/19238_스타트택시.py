'''
틀린이유 1. bfs 탐색 순서를 4방향 탐색의 순서로만 제어하려해서 틀렸다. 내 코드의 경우, 일단 한 cnt가 끝나면 그때
sort를 해서 거리가 같을 때 우선순위를 제어하도록 했다.
틀린이유 2. 문제를 제대로 읽지 않고 택시의 위치와 손님의 위치가 겹칠경우 고려하지 않은채 설계했다.
'''

    # 상 좌 우 하
dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)
DEBUG = False
n, m, gas = map(int, input().split())
mat_origin = [list(map(int, input().split())) for _ in range(n)]
f_y, f_x = map(lambda x:int(x)-1, input().split())
customers = dict()
for _ in range(m):
    s_y, s_x, e_y, e_x = map(lambda x:int(x)-1, input().split())
    customers[(s_y, s_x)] = (e_y, e_x)


def copy():
    mat = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] = mat_origin[i][j]
    return mat


def taxi_to_customer(y, x):
    global gas
    mat = copy()
    if customers.get((y,x)) is not None:
        return y, x, 0
    mat[y][x] = -1
    queue = [(y,x,0)]
    while queue:
        for _ in range(len(queue)):
            y, x, cnt = queue.pop(0)
            if cnt >= gas:
                return False
            for k in range(4):
                ny, nx = y+dy[k], x+dx[k]
                if not(0<=ny<n and 0<=nx<n):
                    continue
                if mat[ny][nx]:
                    continue
                mat[ny][nx] = cnt+1
                queue.append((ny, nx, cnt+1))
        queue.sort(key=lambda xx: (xx[0], xx[1]))
        if DEBUG:
            print(queue)
            for a in mat:
                print(a)
            print()
        for y, x, cnt in queue:
            if customers.get((y,x)) is None:
                continue
            else:
                return y,x,cnt

    return False


def customer_to_goal(y, x):
    global gas
    goal_y, goal_x = customers[(y, x)]
    del customers[(y, x)]
    mat = copy()
    mat[y][x] = -1
    queue = [(y,x,0)]
    while queue:
        for _ in range(len(queue)):
            y, x, cnt = queue.pop(0)
            if cnt >= gas:
                return False
            for k in range(4):
                ny, nx = y+dy[k], x+dx[k]
                if not(0<=ny<n and 0<=nx<n):
                    continue
                if mat[ny][nx]:
                    continue
                if ny == goal_y and nx == goal_x:
                    if DEBUG:
                        print(cnt+1, ny, nx)
                        for a in mat:
                            print(a)
                        print()
                    return ny, nx, cnt+1
                else:
                    mat[ny][nx] = cnt+1
                    queue.append((ny, nx, cnt+1))
                    if DEBUG:
                        print(cnt+1, ny, nx)
                        for a in mat:
                            print(a)
                        print()
    return False
# 1. 스타트 지점부터 bfs로 손님을 태울때까지 탐색한다.
# 1-1. 손님을 태우기 위해 탐색을 하다가 연료가 떨어지면 탐색 종료
# 2. 탐색하다가 손님을 찾으면 일단 태운다.
# 3. 손님을 태운 시점부터 bfs로 그 손님의 목적지 까지 탐색한다.
# 3-1. 목적지까지 가기 위해 탐색을 계속 하다가 연로가 떨어지면 탐색을 종료한다.
# 3-2. 만약 목적지까지 무사히 도착했으면, 손님을 태운 장소부터 목적지까지 사용한 연료의 두배만큼 연료를 채운다.
# 4. 손님을 다 태울때까지 반복한다.


for _ in range(m):
    response = taxi_to_customer(f_y, f_x)
    if response:
        f_y, f_x, cost = response
        gas -= cost
    else:
        print(-1)
        break
    response = customer_to_goal(f_y, f_x)
    if response:
        f_y, f_x, cost = response
        gas += cost
    else:
        print(-1)
        break
else:
    print(gas)
