T = int(input())
for tc in range(1,T+1) :
    result = 0
    N,M = map(int,input().split())
    box = [list(map(int,input().split())) for _ in range(N)]
    houses = [(y,x) for y in range(N) for x in range(N) if box[y][x]]
    print(houses)
    for i in range(N) :
        for j in range(N) :
            count_k = [0]*(2*N-1)
            for y,x in houses :
                count_k[abs(i-y)+abs(j-x)] += 1

            sum_k = sum(count_k)
            print(sum_k)
            print(count_k)
            for k in range(2*N-1,0,-1) :
                if sum_k * M >= (k-1)**2 + k**2 :
                    result = max(result,sum_k)
                sum_k -= count_k[k-1]
    print('#%s %s' % (tc, result))