import sys
import heapq as h
input=sys.stdin.readline
n,m=map(int,input().split())
c=[int(input()) for _ in range(n)]
adj=[[] for _ in range(n)]
for i in range(n):
  temp=[*map(int,input().split())]
  print(temp)
  for j in range(n):
    if temp[j]:
      if c[i]==c[j]:
        adj[i].append((j,temp[j]))
      else:
        adj[i].append((j,temp[j]+10**7))
print(adj)
