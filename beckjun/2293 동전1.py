n, kk = map(int, input().split())

dp = [0] +[0]* kk
print(dp)
for i in range(n):
    dp[int(input())] = 1
print(dp)
for index in range(1, kk+1):
    if index == 1:
        
    for k in range(index//2+1):
            dp[index] += dp[k] * dp[i-k]

print(dp)