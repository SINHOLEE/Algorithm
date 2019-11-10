import sys

def find(u:int)->int:
    if(parent[u] == u) :return u
    parent[u] = find(parent[u])
    return parent[u]

def merge(u:int, v:int):
    u = find(u)
    v = find(v)
    if(u == v): return
    parent[u] = v

N, M = map(int, sys.stdin.readline().split())

parent = [i for i in range(0, N+1)]


for i in range(0, M):
    a,b,c = map(int, sys.stdin.readline().split())
    if(a == 0): merge(b,c)
    else:
        A:int = find(b)
        B:int = find(c)
        if(A == B): sys.stdout.write("YES\n")
        else: sys.stdout.write("NO\n")