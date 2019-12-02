
def fn(depth, dessert,res):
    if n == depth:
        return

    for i in range(m):
        if dessert == i:
            temp = mat[i][depth] // 2
        else:
            temp = mat[i][depth]
        if dp[i][depth] < res + temp:
            dp[i][depth] = res + temp
            fn(depth+1, i,dp[i][depth])
        else:
            return

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(m)]

dp = [[0] * n for _ in range(m)]

fn(0,-1, 0)
for g in dp:
    print(g)
max_val = 0
for a in range(m):
    if max_val < dp[a][n-1]:
        max_val = dp[a][n-1]
print(max_val)