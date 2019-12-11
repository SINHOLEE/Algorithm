import heapq

di = [0,0,-1,1]
dj = [-1,1,0,0]
n,m = map( int, input().split())

DEBUG = False
mat = [list(input()) for _ in range(n)]
visited = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        if mat[i][j] == 'S':
            hq = [(0, 0, 0, i, j)]
            visited[i][j] = 1
        if mat[i][j] == 'F':
            goal = (i, j)
            mat[i][j] = '.'
stop = False
while hq:
    if stop:
        break
    trash, near, cnt, x, y = heapq.heappop(hq)
    if DEBUG:
        print(hq)
        for arr in mat:
            print(arr)

        for arr in visited:
            print(arr)

        print('trash,near,cnt,x,y',trash,near,cnt,x,y)
    for k in range(4):
        newX, newY = x+di[k], y+dj[k]
        if newX == goal[0] and newY == goal[1]:
            print('%s %s' % (trash, near))
            stop = True
            break
        temp_trash, temp_near = trash, near
        if 0<=newX<n and 0<= newY<m:
            if visited[newX][newY] == 0:
                if mat[newX][newY] == 'g':
                    temp_trash+=1
                else:
                    for kk in range(4):
                        newXX,newYY = newX+di[kk], newY+dj[kk]
                        if 0 <= newXX < n and 0 <= newYY < m:
                            if mat[newXX][newYY] == 'g':
                                temp_near+=1
                                break
                visited[newX][newY] = 1
                heapq.heappush(hq, (temp_trash, temp_near, cnt+1, newX, newY))

