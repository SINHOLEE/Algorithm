import heapq
import sys
input = sys.stdin.readline
hq =[]
cnt = 0
for _ in range(int(input())):
    num = int(input())
    if num:
        cnt+=1
        heapq.heappush(hq, -1*num)
    else:
        if cnt:
            cnt-=1
            print(-1 * heapq.heappop(hq))
        else:
            print(0)