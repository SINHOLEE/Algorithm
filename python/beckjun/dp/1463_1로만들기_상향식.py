n = int(input())
temp = 3*n+1
dp = [temp] * temp
dp[1] = 0

for i in range(1, n+1):
    dp[i+1] = min(dp[i+1], dp[i]+1)
    dp[i*2] = min(dp[i*2], dp[i]+1)
    dp[i*3] = min(dp[i*3], dp[i]+1)
print(dp[n])


