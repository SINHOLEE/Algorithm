def solution(strs, t):
    answer = 0
    n_t = len(t)
    dp = [9999999] * (n_t+1)
    dp[0] = 0
    n_strs = len(strs)
    num_strs = [0] * n_strs
    for iii in range(n_strs):
        num_strs[iii] = len(strs[iii])
    for i in range(1, n_t+1):
        for cc in range(n_strs):
            if i-num_strs[cc]< 0:
                continue
            for ii in range(num_strs[cc]):
                if strs[cc][ii] != t[i-num_strs[cc]+ii]:
                    break
            else:
                if dp[i-num_strs[cc]] != 9999999:
                    dp[i] = min(dp[i-num_strs[cc]]+1, dp[i])

    return -1 if dp[len(t)] == 9999999 else dp[len(t)]


print(solution(	["app", "ap", "p", "l", "e", "ple", "pp"], "apple"))

