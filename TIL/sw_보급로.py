import heapq
near = ((1, 0),(0, 1),(-1, 0),(0, -1))

T = int(input())

for t in range(1, T+1):
    n = int(input())

    mat = [list(map(int, input())) for _ in range(n)]
    visited = [[9999999] * n for _ in range(n)]
    hq = [(0,0,0)]
    visited[0][0] = 0

    while hq:
        cnt, y, x = heapq.heappop(hq)
        if y == n-1 and x == n-1:
            break

        for dy, dx in near:
            newY, newX = y+dy, x+dx
            if not (0 <= newY < n and 0 <= newX < n):
                continue
            if visited[newY][newX] > cnt + mat[newY][newX]:
                visited[newY][newX] = cnt + mat[newY][newX]
                heapq.heappush(hq, (cnt+mat[newY][newX], newY, newX))

    print('#%s %s' %(t, cnt))
