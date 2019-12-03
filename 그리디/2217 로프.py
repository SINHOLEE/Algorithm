import sys
input = sys.stdin.readline
n = int(input())
lis = [int(input()) for _ in range(n)]
lis.sort(reverse=True)

val_max = 0
for i in range(1,n+1):
    if i*lis[i-1] > val_max:
        val_max = i*lis[i-1]
print(val_max)