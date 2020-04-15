def solution(strs, t):
    size = len(t)
    dp = [-1]*(size+1)
    dp[0] = 0
    str_set = set(strs)

    for i in range(1, size+1):
        for j in range(1, 6):
            if i-j>=0 and t[i-j:i] in str_set and dp[i-j] != -1:
                if dp[i] == -1:
                    dp[i] = dp[i-j] + 1
                else:
                    dp[i] = min(dp[i], dp[i-j] + 1)
    return dp[-1]