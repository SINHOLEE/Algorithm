import random
from pprint import pprint
matrix_none = []
for x in range(5):
    temp = [0] * 5
    matrix_none += [temp]

# for i in range(5):
#     for j in range(5):
#         matrix[i][j] = random.randint(1, 50)

matrix = [[47, 49, 14, 33, 9],
 [47, 31, 29, 41, 42],
 [19, 3, 5, 26, 12],
 [38, 19, 35, 25, 5],
 [9, 29, 24, 48, 45]]

# pprint(matrix)
# pprint(matrix_none)

dx = [0, 1, 0, -1]  # 오른쪽을 시작으로 시계방향
dy = [1, 0, -1, 0]

# 
# dx *= (5 // 2 + 1)  # 절반 + 1
# dy *= (5 // 2 + 1)



# print(dx)
# print(dy)

# print(len(matrix) * len(matrix[0]))  # 25개의 진행 개수


m_list = []
for ii in range(5):
    for jj in range(5):
        m_list += [matrix[ii][jj]]

# 다시봐라

for i in range(0, len(m_list)-1):
    min = i
    for j in range(i+1, len(m_list)):
        if m_list[min] > m_list[j]:
            min = j
    m_list[i], m_list[min] = m_list[min], m_list[i]

i = 0
j = 0
vector = 0
for x in m_list:
    matrix_none[i][j] = x
    
    new_i = i + dx[vector]
    new_j = j + dy[vector]
    # 오른쪽으로 가라
    if new_j > 4 or new_j < 0 or new_i > 4 or new_i < 0 or matrix_none[new_i][new_j] in m_list:
        vector = (vector + 1) % 4  # 모듈화 ! 중요하다 ㅇ ㅇ
        i += dx[vector]
        j += dy[vector]
          

    else:
        i = new_i
        j = new_j
    # if matrix_none[new_i][new_j] != 0:
        
    
pprint(matrix_none)

# 교수님 풀이는?
