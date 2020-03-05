near = ((0, 1),(0, -1),(1, 0),(-1, 0))

def bfs(y, x):
    q = [(y,x,mat[y][x],1)]

    while q:
        y, x, string, cnt = q.pop(0)
        if cnt == 7:
            my_set.add(string)
            continue

        for dy, dx in near:
            newY, newX = y + dy, x + dx
            if not (0<=newY<4 and 0<=newX<4):
                continue
            q.append((newY, newX, string + mat[newY][newX], cnt + 1))
T = int(input())

for t in range(1,T+1):
    mat = [input().replace(" ", "") for _ in range(4)]

    my_set = set()
    for i in range(4):
        for j in range(4):
            bfs(i, j)
    print('#%s %s'% (t,len(my_set)))