'''
챌린지1. 이진트리를 1차원 배열로 표현하지 않고, 인접리스트로 표현할 때 가중치는 어떻게 처리할 것 인가?
챌린지2. leaf node를 어떻게 판단할 것 인가?
챌린지3. runtime error를 어떻게 처리할 것 인가?
도움: http://www.secmem.org/blog/2019/02/10/TreeDP/
'''

import sys
sys.setrecursionlimit(10000)

n = int(input())

adj_list = [[] for _ in range(n+1)]
adj_val = [[] for _ in range(n+1)]
dp = [0] * (n+1)
maxd = [0] * (n+1)
for _ in range(n-1):
    p, c, w = map(int, input().split())
    adj_list[p].append(c)
    adj_val[p].append(w)
res = 0


def search(u):
    global res
    d = 0
    d2 = 0
    for i in range(len(adj_list[u])):
        v = adj_list[u][i]
        search(v)

        # 왜 첫번째 큰값, 두번째 큰값을 따로 따로 비교하지?
        if d < maxd[v] + adj_val[u][i]:
            d2 = d
            d = maxd[v] + adj_val[u][i]
        elif d2 < maxd[v] + adj_val[u][i]:
            d2 = maxd[v] + adj_val[u][i]

        maxd[u] = max(d, maxd[u])
        dp[u] = max(d + d2, dp[v], dp[u])
    return dp[u]


print(search(1))



