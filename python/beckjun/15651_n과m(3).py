n, m = map(int, input().split())


def dfs(cnt=0, idx=1, res=""):
    global n, m
    if m == cnt:
        print(res)
        return
    for i in range(idx, n+1):
        dfs(cnt+1, i, res+str(i)+' ')


dfs()
