from collections import deque
T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().strip().split())
    mat = [input() for _ in range(n)]
    keys = input()
    visited = [[0] * m for i in range(n)]
    key = 0
    # print()
    v = set()
    for i in keys:
        if i == '0':
            break
        if i in v:
            continue
        v.add(i)
        key ^= 1<<(ord(i)-ord('a'))

    big = set()
    small = set()
    for i in range(ord('a'),ord('z')+1):
        small.add(chr(i))
        big.add(chr(i-32))
    # print(big)
    # print(small)
    starts = []
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                if mat[i][j] != '*':
                    starts.append((i,j))

    print(starts)
    gotten = set()
    dq = deque([])
    for i,j in starts:
        if mat[i][j] not in big:
            if mat[i][j] == '$' and (i,j) not in gotten and visited[i][j] == 0:
                gotten.add((i,j))
                visited[i][j] = 1
                dq.append((i,j, key))
            if visited[i][j] == 0:
                visited[i][j] = 1
                dq.append((i, j, key))
    print(dq)
    print(gotten)

    di = [0,0,-1,1]
    dj = [-1,1,0,0]
    while dq:
        x,y,key = dq.popleft()

        for k in range(4):
            newX, newY = x+di[k], y+dj[k]
            if 0<= newX<n and 0<= newY<m:
                if visited[newX][newY] == 0:
                    if mat[newX][newY] != '*':
                        if mat[newX][newY] == '$':
                            if (newX, newY) not in gotten:
                                gotten.add((newX,newY))
                                visited[newX][newY] = 1
                        elif mat[newX][newY] in small:
                            if key & 1<<(ord(mat[newX][newY])-ord('a')) == 0:
                                temp = key
                                key ^= 1<<(ord(mat[newX][newY])-ord('a'))
                                visited = [[0] * m for i in range(n)]
                            visited[newX][newY] = 1
                            dq.append((newX,newY,key))
                            key = temp
                        elif mat[newX][newY] in big:
                            if key & 1<<(ord(mat[newX][newY])+32 - ord('a')):
                                visited[newX][newY] = 1
                                dq.append((newX, newY, key))
                        else:
                            visited[newX][newY] = 1
                            dq.append((newX, newY, key))
            else:
                for i, j in starts:
                    if mat[i][j] not in big:
                        if mat[i][j] == '$' and (i, j) not in gotten and visited[i][j] == 0:
                            gotten.add((i, j))
                            visited[i][j] = 1
                            dq.append((i, j, key))
                        if visited[i][j] == 0:
                            visited[i][j] = 1
                            dq.append((i, j, key))
    print(gotten)
