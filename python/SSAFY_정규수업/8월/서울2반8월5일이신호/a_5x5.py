import random
from pprint import pprint
# raw = [0] * 5
# matrix = [raw] * 5

    

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         matrix[i][j] = random.randint(1,20)

# pprint(matrix)

matrix = [[1, 1, 1, 1, 1],
          [1, 0, 0, 0, 1],
          [1, 0, 0, 0, 1],
          [1, 0, 0, 0, 1],
          [1, 1, 1, 1, 1]]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

pprint(matrix)
total = 0
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        point = matrix[x][y]
        local_sum = 0
        local_distance = 0
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            # 벽일경우!!!
            if new_x == -1 or new_x == 5 or new_y == -1 or new_y == 5:
                pass
            else:
                temp = point - matrix[new_x][new_y]
                if temp < 0:
                    temp *= -1
                
                local_sum += temp
        total += local_sum
print(total)
