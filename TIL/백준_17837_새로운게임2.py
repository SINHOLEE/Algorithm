dy = (0,0,-1,1)
dx = (1,-1,0,0)

n, k = map(int, input().split())

mat = [[*map(int, input().split())] for _ in range(n)]

board = [[[] for _ in range(n)] for _ in range(n)]
arr = []
for key in range(k):
    y, x, d = map(lambda a : int(a)-1, input().split())
    arr.append((y, x, d, key))
    board[y][x].append(key)

cnt = 0

goal = -1
while True:
    if cnt > 1000:
        break
    if goal != -1:
        goal = cnt
        break

    for y,x,d,ke in arr:

        newY, newX = y+dy[d], x+dx[d]

        #파랑색
        if (not (0 <= newY < n and 0 <= newX < n)) or mat[newY][newX] == 2:
            d ^= 1

            newyy, newxx = y+dy[d], x+dx[d]
            if (not (0 <= newyy < n and 0 <= newxx < n)) or mat[newyy][newxx] == 2:
                arr[ke] = (y, x, d, ke)
            else:
                # 하양
                if mat[newyy][newxx] == 0:
                    arr[ke] = (newyy, newxx, d, ke)

                    for idx in range(len(board[y][x])):
                        if board[y][x][idx] == ke:
                            board[newyy][newxx] += board[y][x][idx:]
                            if len(board[newyy][newxx]) >= 4:
                                goal = 1
                            board[y][x] = board[y][x][:idx]

                            for key1 in board[newyy][newxx]:
                                oy, ox, od, oke = arr[key1]
                                arr[key1] = (newyy, newxx, od, oke)
                            break
                #빨간
                elif mat[newyy][newxx] == 1:
                    arr[ke] = (newyy, newxx, d, ke)

                    for idx in range(len(board[y][x])):
                        if board[y][x][idx] == ke:
                            board[newyy][newxx] += board[y][x][idx:][::-1]
                            if len(board[newyy][newxx]) >= 4:
                                goal = 1

                            board[y][x] = board[y][x][:idx]

                            for key1 in board[newyy][newxx]:
                                oy, ox, od, oke = arr[key1]
                                arr[key1] = (newyy, newxx, od, oke)
                            break
        else:
            # 하양
            if mat[newY][newX] == 0:
                for idx in range(len(board[y][x])):
                    if board[y][x][idx] == ke:
                        board[newY][newX] += board[y][x][idx:]
                        if len(board[newY][newX]) >= 4:
                            goal = 1

                        board[y][x] = board[y][x][:idx]

                        for key1 in board[newY][newX]:
                            oy, ox, od, oke = arr[key1]
                            arr[key1] = (newY, newX, od, oke)
                        break
            # 빨간
            elif mat[newY][newX] == 1:
                for idx in range(len(board[y][x])):
                    if board[y][x][idx] == ke:
                        board[newY][newX] += board[y][x][idx:][::-1]
                        if len(board[newY][newX]) >= 4:
                            goal = 1
                        board[y][x] = board[y][x][:idx]

                        for key1 in board[newY][newX]:
                            oy, ox, od, oke = arr[key1]
                            arr[key1] = (newY, newX, od, oke)
                        break


    cnt += 1

print(goal)