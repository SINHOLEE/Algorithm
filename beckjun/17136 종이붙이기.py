from pprint import pprint
#
mat = []
for i in range(10):
    temp = list(map(int, input().split()))

    mat.append(temp)

pprint(mat)
#
# def check(x, y, a, b, c, d, e, cnt, visited):
#     global min_cnt
#     if min_cnt < cnt:
#         return
#     for i in range(x, 10):
#         for j in range(y, 10):
#             if mat[i][j] and visited[i][j] == False:
#                 visited[i][j] = True
#
#
# pprint(mat)
#
# min_cnt = 26
# check(0, 0, 5, 5, 5, 5, 5, 0, [[False] * 10 for _ in range(10)] )

#
for i in range(1, 1+5):
    for j in range(2, 2+5):
        mat[i][j] = 3

pprint(mat)