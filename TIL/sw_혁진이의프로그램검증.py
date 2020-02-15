def program(y, x, memory, d):
    global flag
    if mat[y][x] == '<':
        return y, x, memory, 0
    if mat[y][x] == '>':
        return y, x, memory, 1
    if mat[y][x] == '^':
        return y, x, memory, 2
    if mat[y][x] == 'v':
        return y, x, memory, 3
    if mat[y][x] == '_':
        if memory == 0:
            return y, x, memory, 1
        else:
            return y, x, memory, 0
    if mat[y][x] == '|':
        if memory == 0:
            return y, x, memory, 3
        else:
            return y, x, memory, 2
    if mat[y][x] == '.':
        return y, x, memory, d
    if mat[y][x] == '@':
        flag = True
        return y, x, memory, d
    if mat[y][x] == '+':
        if memory == 15:
            return y, x, 0, d
        else:
            return y, x, memory + 1, d
    if mat[y][x] == '-':
        if memory == 0:
            return y, x, 15, d
        else:
            return y, x, memory - 1, d

    return y, x, ord(mat[y][x])-ord('0'), d

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())
    mat = [[*map(str, input())] for _ in range(n)]

    visited = [[[[0,0,0,0] for _ in range(16)] for _ in range(m)] for _ in range(n)]
    q = [(0, 0, 0, 1)]
    visited[0][0][0][1] = 1
    flag = False
    while q:

        yy, xx, memoryy, dd = q.pop()
        if mat[yy][xx] == "@":
            flag = True
            break

        if mat[yy][xx] == '?':

            for k in range(4):
                newY, newX = yy + dy[k], xx + dx[k]
                if newY < 0:
                    if visited[n-1][newX][memoryy][k]:
                        continue
                    visited[n - 1][newX][memoryy][k] = 1
                    q.append((n - 1, newX, memoryy, k))
                elif newX < 0:
                    if visited[newY][m-1][memoryy][k]:
                        continue
                    visited[newY][m - 1][memoryy][k]=1
                    q.append((newY, m - 1, memoryy, k))
                elif newY >= n:
                    if visited[0][newX][memoryy][k]:
                        continue
                    visited[0][newX][memoryy][k] = 1
                    q.append((0, newX, memoryy, k))
                elif newX >= m:
                    if visited[newY][0][memoryy][k]:
                        continue
                    visited[newY][0][memoryy][k]=1
                    q.append((newY, 0, memoryy, k))
                else:
                    if visited[newY][newX][memoryy][k]:
                        continue
                    visited[newY][newX][memoryy][k] = 1
                    q.append((newY, newX, memoryy, k))

        else:
            y, x, memory, d = program(yy, xx, memoryy, dd)

            newY, newX = y+dy[d], x+dx[d]
            if newY < 0:
                if visited[n-1][newX][memory][d]:
                    continue
                visited[n-1][newX][memory][d] = 1
                q.append((n-1, newX, memory, d))
            elif newX < 0:
                if visited[newY][m-1][memory][d]:
                    continue
                visited[newY][m-1][memory][d] = 1
                q.append((newY, m-1, memory, d))
            elif newY >= n:
                if visited[0][newX][memory][d]:
                    continue
                visited[0][newX][memory][d] = 1
                q.append((0, newX, memory, d))
            elif newX >= m:
                if visited[newY][0][memory][d]:
                    continue
                visited[newY][0][memory][d] = 1
                q.append((newY, 0, memory, d))
            else:
                if visited[newY][newX][memory][d]:
                    continue
                visited[newY][newX][memory][d] = 1
                q.append((newY, newX, memory, d))

    if flag:
        print('#%s YES' % t)
    else:
        print('#%s NO' % t)

