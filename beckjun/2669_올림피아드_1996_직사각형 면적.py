from pprint import pprint

mat = [[0] * 101 for _ in range(101)]


for j in range(4):
    num = list(map(int, input().split()))
    for x in range(num[0], num[2]):
        for y in range(num[1], num[3]):
            if mat[x][y] == 0:
                mat[x][y] += 1
count = 0
for xx in range(len(mat)):
    for yy in range(len(mat[xx])):
        if mat[xx][yy] == 1:
            count += 1

print(count)