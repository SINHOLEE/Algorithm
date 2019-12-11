n = int(input())

dp = [0] * n
dp[1] = 1
for i in range(2, n):
    if dp[i-1] + dp[i-2] >= n:
        break
    dp[i] = dp[i-1] + dp[i-2]
print(sum(map(lambda x: x % 2 == 0, dp)))