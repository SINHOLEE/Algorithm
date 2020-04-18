def dp(num, memo):
    if num == 1:
        return 1
    if num == 2:
        return 1
    if memo[num]:
        return memo[num]
    memo[num] = dp(num-2, memo) + dp(num-1, memo)
    return memo[num]


def solution(N):
    memo = [0, 1, 1] + [0] * N
    return dp(N+2, memo) * 2


print(solution(80))

