n,k = map(int,input().split())

visited = [0]*100001
queue = [(n,1)]
visited[n]=1
while queue:
    target, cnt = queue.pop(0)
    if(target==k):break
    newT = 2*target
    while newT<=100000:
        
        if not visited[newT]:
            queue.append((newT,cnt))
            visited[newT]=cnt
        else:
            break
        newT*=2
    if target-1>=0 and not visited[target-1]:
        queue.append((target-1,cnt+1))
        visited[target-1]=cnt+1
    if target+1<=100000 and not visited[target+1]:
        queue.append((target+1,cnt+1))
        visited[target+1]=cnt+1

print(visited[k]-1)
