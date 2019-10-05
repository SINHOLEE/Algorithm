from pprint import pprint

n, k = map(int, input().split())
dolls = list(map(int, input().split()))

mat_x = [[0] * (n+1) for _ in range(n+1)]
mat_xx = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            mat_x[i][j] = dolls[i-1]
            mat_xx[i][j] = dolls[i-1] * dolls[i-1]
        elif i < j:
            mat_x[i][j] = mat_x[i][j-1] + dolls[j-1]
            mat_xx[i][j] = mat_xx[i][j-1] + dolls[j-1] * dolls[j-1]

my_min = 999
for m in range(k-1, n):
    for i in range(1, n-m+1):
        ex2 = mat_xx[i][i+m] / (m+1)
        ex = (mat_x[i][i+m] / (m+1)) ** 2
        sd = abs(ex2 - ex) ** (0.5)
        print(sd)
        if sd < my_min:
            my_min = sd
print(round(my_min, 11))