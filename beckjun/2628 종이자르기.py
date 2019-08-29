from pprint import pprint

J, I = input().split()
J, I = int(J), int(I)

row = [0]  # i 가로
col = [0]  # j 세로
# mat = [[0] * J for i in range(I)]
#
# pprint(mat)
T = int(input())
for t in range(T):
    # dr = 0 가로, dr=1 세로
    # cut : 잘라지는 점선의 번호
    dr, cut = input().split()
    dr, cut = int(dr), int(cut)
    if dr:
        col += [cut]
    else:
        row += [cut]

row += [I]
col += [J]
row.sort()
col.sort()

max_area = 0
for r_idx in range(len(row)-1):
    width = row[r_idx + 1] - row[r_idx]
    for c_idx in range(len(col)-1):
        height = col[c_idx + 1] - col[c_idx]
        area = width * height
        if area >= max_area:
            max_area = area
print(max_area)
