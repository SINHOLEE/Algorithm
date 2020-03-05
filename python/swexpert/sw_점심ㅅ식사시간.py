def move(y, x, stair_n, peop):
    global min_time
    dist = []
    for yy, xx in peop:
        dist.append(abs(yy-y)+abs(xx-x))
    dist.sort()
    cnt = 0
    q = []
    while True:
        if min_time <= cnt:
            return cnt
        if len(dist) == 0 and len(q) == 0:
            break
        for i in range(len(q)):
            q[i] -= 1
        for j in range(len(dist)):
            dist[j] -= 1

        while True:
            if len(q) == 0:
                break
            if q[0] > 0:
                break
            q.pop(0)

        while True:
            if len(dist) == 0:
                break
            if len(q) == 3:
                break
            if dist[0] >= 0:
                break
            dist.pop(0)
            q.append(stair_n)
        cnt+=1

    return cnt




def subset(depth, a, b):
    global min_time
    if depth == len(people):
        min_time = min(
            min_time,
            max(
                move(entries[0][0],entries[0][1],entries[0][2], a),
                move(entries[1][0],entries[1][1],entries[1][2], b)
                )
        )
        return

    subset(depth+1, a+[people[depth]], b)
    subset(depth+1, a, b+[people[depth]])
T = int(input())

for t in range(1, 1+T):
    n = int(input())
    mat = [[*map(int, input().split())] for _ in range(n)]

    people = []
    entries = []
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1:
                people.append((i, j))
            if mat[i][j] > 1:
                entries.append((i, j, mat[i][j]))

    min_time = 987654321
    subset(0, [], [])
    #
    print('#%s %s' % (t, min_time))