T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())
    mat = [[*map(int, input().split())] for _ in range(n)]
    max_res = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            temp = 0
            for ii in range(i, i+m):
                for jj in range(j, j+m):
                    temp += mat[ii][jj]
            max_res = max(max_res, temp)
    print('#%s %s' % (t, max_res))