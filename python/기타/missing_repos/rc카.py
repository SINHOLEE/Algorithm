T=int(input())
for t in range(1, T+1):
    n=int(input())
    sum=0
    fast=0
    for i in range(n):
        temp=list(map(int, input().split()))
    if temp[i][0]==1:
        sum=fast+temp[i][1]
    elif temp[i][0]==2:
        if fast-temp[i][1]<=0:
            continue
        else:
            sum=fast+temp[i][1]
    elif temp[i][0]==0:
        sum=fast
    print('#%s %d'%(t,sum))
