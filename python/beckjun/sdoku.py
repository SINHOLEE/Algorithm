from pprint import pprint
import copy


def check_fine(i, j, mat):
    check = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}  
   
    temp = copy.copy(check)
    for jj in range(9):
        temp[mat[i][jj]] += 1
        if temp[mat[i][jj]] > 1:
            return False


    temp = copy.copy(check)
    for ii in range(9):
        temp[mat[ii][j]] += 1
        if temp[mat[ii][j]] > 1:
            return False

    for unit_3by3 in check_3by3:
        for y, x in unit_3by3:
            if y == i and x == j:
                temp = copy.copy(check)
                for y, x in unit_3by3:
                    temp[mat[y][x]] += 1
                    if temp[mat[y][x]] > 1:
                        return False
 
                break
    return True

matt = [list(map(int, input().split())) for _ in range(9)]
print(matt)

tem = [(0,1,2), (3, 4, 5), (6, 7, 8)]

check_3by3 = []

for a in tem:
    for b in tem:
        temp = []
        for i in a:
            for j in b:
                temp.append((i, j))
        check_3by3.append(temp)

print(check_fine(2,2, matt))