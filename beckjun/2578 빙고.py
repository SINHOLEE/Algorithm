def check_bingo(matrix):
    count = 0
    for i in range(5):
        if matrix[i] == [0, 0, 0, 0, 0]:
            count += 1

    for i in range(5):
        zero_count = 0
        for j in range(5):
            if matrix[j][i] == 0:
                zero_count += 1
        if zero_count == 5:
            count += 1

    zero_count = 0
    for i in range(5):
        if matrix[i][i] == 0:
            zero_count += 1
    if zero_count == 5:
        count += 1

    zero_count = 0
    for i in range(5):
        if matrix[i][4-i] == 0:
            zero_count += 1
    if zero_count == 5:
        count += 1

    return count

my_mat = []
my_list = ['x'] + ([[]] * 25)
for i in range(5):
    temp = list(map(int, input().split()))
    my_mat += [temp]
    for j in range(len(temp)):
        my_list[temp[j]] = [i, j]

result = 0
for x in range(5):
    bingo = list(map(int, input().split()))
    for y in range(len(bingo)):
        my_mat[my_list[bingo[y]][0]][my_list[bingo[y]][1]] = 0
        if check_bingo(my_mat) >= 3:
            result = (x * 5) + y + 1
            break

    if result:
        break
    else:
        pass


print(result)

