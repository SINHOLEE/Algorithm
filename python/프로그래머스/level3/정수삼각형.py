def dp(row, col):
    global memo, tr
    if row == len(tr):
        return 0
    if memo[row][col]:
        return memo[row][col]
    memo[row][col] = \
        tr[row][col] + \
        max(dp(row+1, col), dp(row+1, col+1))
    return memo[row][col]


def solution(triangle):
    global memo, tr
    tr = triangle
    memo = []
    for a in triangle:
        memo.append([0] * len(a))
    answer = dp(0, 0)
    print(answer)
    return answer


memo = []
tr = []
solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])