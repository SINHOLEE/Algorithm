n, m = map(int, input().split())
lis = list(map(int, input().split()))
visited = [0] * (max(lis)+1)
for num in lis:
    visited[num] += 1


def dfs(cnt=0, idx=0, res=""):
    global n, m
    if m == cnt:
        print(res)
        return
    for i in range(idx, max(lis)+1):
        if visited[i] == 0:
            continue
        dfs(cnt+1, i, res+str(i)+' ')


dfs()
