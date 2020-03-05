from collections import deque
n,a,b = map(int,input().split())

x, y = min(a,b), max(a,b)
visited = [0]
min_cnt = -1
def bfs(x,y):
    global min_cnt
    dq = deque([(x,y,0)])
    while dq:
        xx,yy,cnt = dq.popleft()

        if xx == yy:
            min_cnt = cnt
            break
        if 0<xx+2**cnt<n+1 and 0<yy+2**cnt<n+1:
            if xx+2**cnt <= yy+2**cnt:
                if visited.get(cnt+1) == None:
                    visited.update({cnt+1:(xx+2**cnt, yy+2**cnt)})
                    dq.append((xx+2**cnt, yy+2**cnt, cnt+1))
                else:
                    if visited[cnt+1][0] == xx+2**cnt and visited[cnt+1][1] ==  yy+2**cnt:
                        pass
                    else:
                        visited.update({cnt + 1: (xx + 2 ** cnt, yy + 2 ** cnt)})
                        dq.append((xx + 2 ** cnt, yy + 2 ** cnt, cnt + 1))
        if 0<xx+2**cnt<n+1 and 0<yy-2**cnt<n+1:
            if xx+2**cnt <= yy-2**cnt:
                if visited.get(cnt + 1) == None:
                    visited.update({cnt + 1: (xx + 2 ** cnt, yy - 2 ** cnt)})
                    dq.append((xx + 2 ** cnt, yy - 2 ** cnt, cnt + 1))
                else:
                    if visited[cnt + 1][0] == xx + 2 ** cnt and visited[cnt + 1][1] == yy - 2 ** cnt:
                        pass
                    else:
                        visited.update({cnt + 1: (xx + 2 ** cnt, yy - 2 ** cnt)})
                        dq.append((xx + 2 ** cnt, yy - 2 ** cnt, cnt + 1))
        if 0<xx-2**cnt<n+1 and 0<yy+2**cnt<n+1:
            if xx-2**cnt <= yy+2**cnt:
                if visited.get(cnt+1) == None:
                    visited.update({cnt+1:(xx-2**cnt, yy+2**cnt)})
                    dq.append((xx-2**cnt, yy+2**cnt, cnt+1))
                else:
                    if visited[cnt+1][0] == xx-2**cnt and visited[cnt+1][1] ==  yy+2**cnt:
                        pass
                    else:
                        visited.update({cnt + 1: (xx - 2 ** cnt, yy + 2 ** cnt)})
                        dq.append((xx - 2 ** cnt, yy + 2 ** cnt, cnt + 1))
        if 0<xx-2**cnt<n+1 and 0<yy-2**cnt<n+1:
            if xx-2**cnt <= yy-2**cnt:
                if visited.get(cnt + 1) == None:
                    visited.update({cnt + 1: (xx - 2 ** cnt, yy - 2 ** cnt)})
                    dq.append((xx - 2 ** cnt, yy - 2 ** cnt, cnt + 1))
                else:
                    if visited[cnt + 1][0] == xx - 2 ** cnt and visited[cnt + 1][1] == yy - 2 ** cnt:
                        pass
                    else:
                        visited.update({cnt - 1: (xx - 2 ** cnt, yy - 2 ** cnt)})
                        dq.append((xx - 2 ** cnt, yy - 2 ** cnt, cnt + 1))
bfs(x,y)

print(min_cnt)