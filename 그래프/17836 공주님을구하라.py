from collections import deque
n,m,t = map(int, input().strip().split())
DEBUG = False
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
mat = [list(map(int, input().strip().split())) for _ in range(n)]
for i in range(n):
    for j in  range(m):
        if mat[i][j]:
            mat[i][j] *= -1
# bfs
        # x, y, cnt, hassord
q = deque([(0,0,0,False)])
goal = []
while q:
    x,y,cnt,hassord = q.popleft()
    if cnt > t:
        break
    if DEBUG:
        print(hassord)
        for arr in mat:
            print(arr)
    if x==n-1 and y==m-1:
        goal.append(cnt)
        continue
    for k in range(4):
        new_x, new_y = x+di[k], y+dj[k]
        if 0<=new_x<n and 0<=new_y<m and not(new_y==0 and new_x==0) and (mat[new_x][new_y] == 0 or mat[new_x][new_y] == -2):
            if mat[new_x][new_y] == -2:
                mat[new_x][new_y] = cnt + 1
                goal_dis = abs(new_y-(m-1)) +abs(new_x-(n-1))
                q.append((n-1,m-1,mat[new_x][new_y]+goal_dis,True))
            else:
                mat[new_x][new_y] = cnt + 1
                q.append((new_x,new_y,mat[new_x][new_y],False))
if len(goal) == 0:
    print('Fail')
else:
    res = min(goal)
    if res > t:
        print('Fail')
    else:
        print(res)