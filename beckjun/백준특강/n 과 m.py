def perm(depth, lis):
    if depth == m:
        print(' '.join(map(str,lis)))
        return
    for j in range(1,n+1):
        if visited[j] == 0:
            visited[j] = 1
            perm(depth+1, lis + [j])
            visited[j] = 0
n,m = map(int, input().split())

visited = [0] * (n+1)
perm(0, [])