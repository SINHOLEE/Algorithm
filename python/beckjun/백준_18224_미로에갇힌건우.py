from collections import deque
import heapq
def move(x,y, dx, dy):
    ox, oy = x, y
    while True:
        if not (0<= x< n and 0<= y < n):
            return ox, oy
        if mat[x][y] == 0:
            return x, y
        if mat[x][y] == -1:
            x, y = x+dx, y+dy
            continue
        if mat[x][y] > 0:
            return ox, oy


n, m = map(int, input().split())

mat = [[*map(lambda x:-int(x), input().split())] for _ in range(n)]
visited = [[[0, 0] for _ in range(n)] for _ in range(n)]
visited[0][0][0] = 1
hq = []
heapq.heappush(hq,(1, 0, 0, 2))
near = ((0, -1), (0, 1), (1, 0), (-1, 0))
goal = False
while hq:
    if goal:
        break
    cnt, x, y, time = heapq.heappop(hq)

    wall_list = False
    flag = False
    for di, dj in near:
        temp = time
        newX, newY = x+di, y+dj
        if not (0 <= newX < n and 0 <= newY < n):
            continue
        if time == 3: # 밤
            if mat[newX][newY] == -1:
                newX, newY = move(newX, newY, di, dj)
        else:
            if mat[newX][newY] == 0:
                flag = True

        if mat[newX][newY] == -1:
            wall_list = True
            continue
        if visited[newX][newY][0] and visited[newX][newY][1] :
            continue
        if time == 2 and visited[newX][newY][0] > 0:
            continue
        if time ==3 and visited[newX][newY][1] > 0:
            if visited[newX][newY][1] < cnt + 1:
                continue
        if (cnt) % m == 0:
            temp = time^1
        if newX == n - 1 and newY == n - 1:
            goal = True
            break
        visited[newX][newY][temp-2] = cnt + 1
        heapq.heappush(hq,(cnt+1, newX, newY, temp))

    if flag and wall_list:
        if m-((cnt) % m): #odd
            if 0< visited[x][y][1] < cnt+ m-((cnt) % m) + 1:
                continue
            visited[x][y][1] = cnt+ m-((cnt) % m) + 1
            heapq.heappush(hq, (cnt+ m-((cnt) % m) + 1, x, y, 3))
        else:
            if 0<visited[x][y][1] < cnt+ m-((cnt) % m) :
                continue

            visited[x][y][1] = cnt + m-((cnt) % m)
            heapq.heappush(hq, (cnt  + m-((cnt) % m), x, y, 3))



if goal:
    if time == 2:
        print(((cnt-1) // (2 * m)) + 1, 'sun')
    else:
        print(((cnt-1) // (2 * m)) + 1, 'moon')

else:
    print(-1)







