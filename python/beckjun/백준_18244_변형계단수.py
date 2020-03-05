# n = int(input())
#
# def recursion(front, back, depth, danjo, lis):
#     global cnt
#
#     cnt += 1
#     if danjo >= 3:
#         return
#     if depth == n-1:
#         return
#     if front == -1:
#         if 0<= back+1 <= 9:
#             recursion(back, back + 1, depth + 1, danjo + 1, lis + [back+1])
#         if 0<= back-1 <= 9:
#             recursion(back, back - 1, depth + 1, danjo + 1, lis + [back-1])
#     else:
#         if back - front == 1:
#             if 0<= back+1 <= 9:
#                 recursion(back, back + 1, depth + 1, danjo + 1, lis + [back+1])
#             if 0<= back-1 <= 9:
#                 recursion(back, back - 1, depth + 1, 0, lis + [back-1])
#         elif front - back == 1:
#             if 0 <= back + 1 <= 9:
#                 recursion(back, back + 1, depth + 1, 0, lis + [back+1])
#             if 0 <= back - 1 <= 9:
#                 recursion(back, back - 1, depth + 1, danjo + 1, lis + [back-1])
# cnt = 0
# for i in range(1):
#     recursion(-1, i, 0, 0, [i])
#
# print(cnt)
print(2 ** 100