T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())
    mat = [input() for _ in range(n)]
    min_cnt = 999999999
    for a in range(1, n-1):
        for b in range(a+1, n):
            cnt = 0
            # w
            for y1 in range(0, a):
                for x1 in range(m):
                    if mat[y1][x1] != "W":
                        cnt += 1

            #b
            for y2 in range(a, b):
                for x2 in range(m):
                    if mat[y2][x2] != "B":
                        cnt += 1
            #r
            for y3 in range(b, n):
                for x3 in range(m):
                    if mat[y3][x3] != "R":
                        cnt += 1
            min_cnt = min(min_cnt, cnt)
            
    print('#%s %s' % (t, min_cnt))