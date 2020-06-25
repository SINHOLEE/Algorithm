from pprint import pprint
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    target = n ** 2
    x = 1
    i = 0
    j = 0
    visited = [[False] * n for _ in range(n)]
    direction = 0
    while True:
        visited[i][j] = x
        if x == n**2:
            break
        if i+di[direction] < 0 or j+dj[direction] < 0 or i+di[direction] > n-1 or j+dj[direction] > n -1 or visited[i+di[direction]][j+dj[direction]] != False:
            direction = (1 + direction) % 4
        i += di[direction]
        j += dj[direction]
        x += 1

    print('#%s' % tc)
    for a in range(n):
        print(' '.join(map(str, visited[a])))

# ipput data
# 1
# 10

