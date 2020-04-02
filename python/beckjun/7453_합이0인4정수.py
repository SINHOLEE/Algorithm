import sys
input = sys.stdin.readline
n = int(input())

mat = [[0] * 4 for _ in range(n)]
for _ in range(n):
    a, b, c, d = map(int,input().split())
    mat[_][0] = a
    mat[_][1] = b
    mat[_][2] = c
    mat[_][3] = d

a_dic = {}

for i in range(n):
    for j in range(n):
        a = mat[i][0] + mat[j][1]
        if a_dic.get(a) is None:
            a_dic[a] = 1
        else:
            a_dic[a] += 1

res = 0
for i in range(n):
    for j in range(n):
        k = mat[i][2] + mat[j][3]
        if a_dic.get(-1 * k) is not None:
            res += a_dic[-1 * k]


print(res)
