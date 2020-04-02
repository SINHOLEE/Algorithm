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

a_list = [0] * (n * n)
b_list = [0] * (n * n)

for i in range(n):
    for j in range(n):
        a_list[n * i + j] = mat[i][0] + mat[j][1]
        b_list[n * i + j] = mat[i][2] + mat[j][3]

a_list.sort()
b_list.sort()

s = 0
e = n*n-1
res = 0
while s <= n*n-1 and e >= 0:
    temp = a_list[s] + b_list[e]
    if temp == 0:
        left_cnt = 0
        for i in range(s, n*n):
            if a_list[i] == a_list[s]:
                left_cnt += 1
            else:
                break

        right_cnt = 0
        for i in range(e, -1, -1):
            if b_list[i] == b_list[e]:
                right_cnt += 1
            else:
                break
        res += left_cnt * right_cnt
        s += left_cnt
        e -= right_cnt
    elif temp > 0:
        e -= 1
    else:
        s += 1
print(res)
