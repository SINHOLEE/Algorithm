# from collections import deque
# import sys
# input = sys.stdin.readline
#
# near = ((0, 1), (1, 0), (0, -1), (-1, 0))
#
# n, m = map(int, input().split())
# sy, sx = map(int, input().split())
# ey, ex = map(int, input().split())
# mat = [[*map(int, input().split())] for _ in range(n)]
#
# visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
# q = deque([(sy-1, sx-1, 0, 0)])
# visited[sy-1][sx-1][0] = 1
#
# res = -1
# while q:
#     y, x, magic, cnt = q.popleft()
#
#     if y == ey-1 and x == ex-1:
#         res = cnt
#         break
#     for dy, dx in near:
#         ny, nx = y + dy, x + dx
#
#         if not(0<=ny<n and 0<=nx<m):
#             continue
#
#         if mat[ny][nx]:
#             if magic:
#                 continue
#             if visited[ny][nx][1]:
#                 continue
#
#             q.append((ny, nx, 1, cnt+1))
#             visited[ny][nx][1] = cnt+1
#         else:
#             if visited[ny][nx][magic]:
#                 continue
#             q.append((ny, nx, magic, cnt+1))
#             visited[ny][nx][magic] = cnt+1
#
#
# print(res)



def re(i):
    if i == 300:
        return
    re(i+1)
re(0)