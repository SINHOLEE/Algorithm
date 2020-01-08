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
    cnt = 0
    pivot = 0
    while True:
        visited[i][j] = x

        if x == n**2:
            break
        if i+di[pivot] < 0 or j+dj[pivot] < 0 or i+di[pivot] > n-1 or j+dj[pivot] > n -1 or visited[i+di[pivot]][j+dj[pivot]] != False:
            pivot = (1 + pivot) % 4
            cnt += 1
        i += di[pivot]
        j += dj[pivot]
        x += 1

    print('#%s' % tc)
    for a in range(n):
        print(' '.join(map(str, visited[a])))

    print(cnt)


