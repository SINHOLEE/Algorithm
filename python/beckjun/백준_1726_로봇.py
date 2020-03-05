'''
1. 제발 동서남북 순서 이상하게 받지 말자...
두번 세번확인
2. 입력받는값이 내가 쓰는 인덱스와 통일시켰는지 체크

'''


n,m = map(int, input().split())
    #동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

turn = {
    0 : [2, 3],
    1 : [2, 3],
    2 : [0, 1],
    3 : [0, 1]
}

mat = [[*map(int, input().split())] for _ in range(n)]

sy, sx, d = map(int, input().split())
ey, ex, ed = map(int, input().split())

visited = [[[0]*4 for _ in range(m)] for _ in range(n)]

q = [(sy-1, sx-1, d-1, 1)]
visited[sy-1][sx-1][d-1] = 1
while q:
    y, x, d , cnt= q.pop(0)
    if y == ey-1 and x == ex-1 and d == ed-1:
        print(cnt-1)
        break
    # go
    for go in range(1, 4):
        newY, newX = y + go * dy[d], x + go * dx[d]
        if not (0 <= newY < n and 0 <= newX < m):
            continue
        if visited[newY][newX][d]:
            continue
        tempY, tempX = y, x
        c = 0
        for z in range(go):
            tempY, tempX = tempY + dy[d], tempX + dx[d]
            if mat[tempY][tempX]:
                c+=1
        if c == 0:
            visited[newY][newX][d] =  cnt + 1
            q.append((newY, newX, d, cnt + 1))

    for newd in turn[d]:
        if visited[y][x][newd]:
            continue
        visited[y][x][newd] =  cnt +1
        q.append((y, x, newd, cnt + 1))


