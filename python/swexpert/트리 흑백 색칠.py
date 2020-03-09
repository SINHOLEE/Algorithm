# color 0 == w, 1 == b
def solution(node, color, prev):
    if dp[color][node] != -1:
        return dp[color][node]

    if len(adj_list[node]) == 1 and adj_list[node][0] == prev:
        dp[color][node] = 1
        return 1
    temp = 1
    for nxt in adj_list[node]:
        if nxt == prev:
            continue
        if color:
            temp *= solution(nxt, 0, node)
        else:
            temp *= solution(nxt, 0, node) + solution(nxt, 1, node)

    dp[color][node] = temp
    return temp


for t in range(1, int(input())+1):
    n = int(input())
    adj_list = [[]for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)
    dp = [[-1] * (n+1) for _ in range(2)]
    res = (solution(n, 0, 0) + solution(n, 1, 0)) % 1000000007
    print("#%s %s" % (t, res))
