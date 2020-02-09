import heapq

n = int(input())

mat = [[*map(int, input().split())] for _ in range(n)]

start = (0, 1)
        #가로 세로 대각
dy = (0,1,1)
dx = (1, 0, 1)
direction = {
    0 : (0, 2),
    1 : (1, 2),
    2 : (0, 1, 2)
}
cnt=0
total = 0
q = [(0, 1, 0)]
visited = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
visited[0][1][0] = 1
while q:
#    # dp wrong
#     y, x, d = q.pop(0)
#     for k in direction[d]:
#         newY, newX = y + dy[k], x + dx[k]
#         if not (0<=newY<n and 0<= newX<n):
#             continue
#         if mat[newY][newX]:
#             continue
#         if k == 2:
#             if mat[newY][newX-1] or mat[newY-1][newX]:
#                 continue
#         if visited[newY][newX][k] > 0:
#             visited[newY][newX][k] = visited[y][x][d]+visited[newY][newX][k]
#             continue
#         visited[newY][newX][k] = visited[y][x][d]
#
#         q.append((newY, newX, k))
# print(sum(visited[n - 1][n - 1]))
#     #dfs
    y, x, d = q.pop()
    if y == n - 1 and x == n - 1:
        cnt += 1
        continue

    for k in direction[d]:
        newY, newX = y + dy[k], x + dx[k]
        if not (0 <= newY < n and 0 <= newX < n) or mat[newY][newX]:
            continue
        if k == 2:
            if mat[newY][newX - 1] or mat[newY - 1][newX]:
                continue
        q.append((newY, newX, k))
print(cnt)
