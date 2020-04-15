# from collections import deque
# n, m = map(int, input().split())
# mat = [input() for _ in range(n)]

# di = [0, 0, -1, 1]
# dj = [-1, 1, 0, 0]

# for i in range(n):
#     for j in range(m):
#         if mat[i][j] == '0':
#             start = (i, j)
#             mat[i] = mat[i].replace('0', '.')

# keys = [[[0]*(2**6) for i in range(m)] for _ in range(n)]

# dq = deque([(0, 0, start[0], start[1])])
# keys[start[0]][start[1]][0] = 1

# flag = True
# while dq:
#     cnt, key, x, y = dq.popleft()

#     if mat[x][y] == '1':
#         flag = False
#         break
#     temp = key
#     for k in range(4):
#         newX, newY = x+di[k], y+dj[k]
#         if 0 <= newX < n and 0 <= newY < m:
#             if keys[newX][newY][key]:
#                 continue
#             if mat[newX][newY] != '#':
#                 if mat[newX][newY] in ('a', 'b', 'c', 'd', 'e', 'f'):
#                     if key & 1 << (ord(mat[newX][newY]) - ord('a')) == 0:
#                         temp = key
#                         key = key | 1 << (ord(mat[newX][newY]) - ord('a'))

#                 elif mat[newX][newY] in ('A', 'B', 'C', 'D', 'E', 'F'):
#                     if key & 1 << (ord(mat[newX][newY]) - ord('A')) == 0:
#                         continue
#                 keys[newX][newY][key] = 1
#                 dq.append((cnt+1, key, newX, newY))
#                 key = temp
# if flag:
#     print(-1)
# else:
#     print(cnt)

print(4&1<<1)

print(4 | 1<<1)
