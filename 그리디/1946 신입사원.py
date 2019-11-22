T =  int(input())
for t in range(T):
    n = int(input())
    lis = [list(map(int, input().split())) for _ in range(n)]
    lis.sort(key=lambda x:(x[0], x[1]))
    cnt = 1
    # print(lis)
    for i in range(n-1):
        if  lis[i][1] > lis[i+1][1]:
            continue
        cnt+=1
    print(cnt)
