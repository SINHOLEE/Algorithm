
import sys
sys.setrecursionlimit(200000)

n,m = map(int, input().split())
visited = [0]*(n+1)
adj_list = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    adj_list[b].append(a)
target = int(input())

cnt = 0
def traversal(node):
    global cnt
    for n in adj_list[node]:
        if visited[n]:continue
        visited[n]=1
        cnt+=1
        traversal(n)
visited[target]
traversal(target)
print(cnt)
