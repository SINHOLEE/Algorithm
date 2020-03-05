T = int(input())
def distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


def perm(x1, y1, depth, distan):
    global min_dis, cnt
    cnt += 1
    if depth == N:
        distan += distance(x1,  y1, home[0], home[1])
        if min_dis > distan:
            min_dis = distan
        return
    if min_dis <= distan:
        return
    for k in range(0, N):
        if visited[k] == False:
            visited[k] = True
            x2, y2 = nodes[k][0], nodes[k][1]
            perm(x2, y2, depth+1, distan + distance(x1, y1,x2, y2))
            visited[k] = False

for tc in range(1, T+1):
    N = int(input())
    nodes = list(map(int, input().split()))
    company = (nodes[0], nodes[1])
    home = (nodes[2], nodes[3])
    nodes = nodes[4:]
    nodes = [(nodes[x], nodes[x+1]) for x in range(0,len(nodes),2)]
    visited = [False] * N
    min_dis = 99999999999
    cnt = 0

    perm(company[0], company[1], 0, 0)

    print('#%s %s' % (tc, min_dis))
    print(cnt)

