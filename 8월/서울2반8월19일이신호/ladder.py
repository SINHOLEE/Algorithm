from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open('output.txt', 'w', encoding='utf-8')
def iswall(i, j):
    if i <= -1 or i >= 100 or j <= -1 or j >= 100:
        return True
    else:
        return False
from pprint import pprint

mat = [[1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
      [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
      [1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
      [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
      [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
      [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
      [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
      [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
      [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
      [1, 0, 2, 0, 1, 0, 0, 0, 0, 1]]
    # 좌 우 상
id = [0, 0, -1]
jd = [-1, 1, 0]
# j = 우리가 원하는 인덱스
def iswall(i, j):
    if i < 0 or i > 9 or j < 0 or j > 9:
        return True
    else:
        return False
i = 9 # len(mat)
j = 0
direction_i = 0
direction_j = 0
left = False
right = False


for x in range(len(mat[9])):
    if mat[9][x] == 2:
        j = x
        while i != 0:
            # 좌, 우측 조사
            for check in range(2):
                i += id[check]
                j += jd[check]
                if (not iswall(i, j)) and (mat[i][j] == 1):
                    if check == 0:
                        left = True
                        i -= id[check]
                        j -= jd[check]
                    elif check == 1:
                        right = True
                        i -= id[check]
                        j -= jd[check]
                else:
                    i -= id[check]
                    j -= jd[check]
            if direction_j == 0 and direction_i == 0:
                #  만약 왼쪽에만 1이 있다면 왼쪽으로 가 그리고 이전방향을 왼쪽으로 줘
                if left == True and right == False:
                    i += id[0]
                    j += jd[0]
                    direction_i = id[0]
                    direction_j = jd[0]
                #  만약 오른쪽에만 1이 있다면 오른쪽으로 가 그리고 이전방향을 오른쪽으로 줘
                elif left == False and right == True:
                    i += id[1]
                    j += jd[1]
                    direction_i = id[1]
                    direction_j = jd[1]
                # 만약 양쪽 다 0이면 위로 올라가고 이전방향을 0으로 줘
                elif left == False and right == False:
                    i += id[2]
                    j += jd[2]
                    direction_j = 0
                    direction_i = 0
            # 만약 이전 방향이 왼쪽일 때
            elif direction_i == id[0] and direction_j == jd[0]:
                # 위로 가고 이전방향 0으로 줘
                if left == False and right == True:
                    i += id[2]
                    j += jd[2]
                    direction_j = 0
                    direction_i = 0
                # 양쪽이 1이면 이전방향으로 진행해
                elif left == True and right == True:
                    i += direction_i
                    j += direction_j
            # 만약 이전방향이 오른쪽일 때
            elif direction_i == id[1] and direction_j == jd[1]:
                # 위로 가고 이전방향을 0으로 줘
                if left == True and right == False:
                    i += id[2]
                    j += jd[2]
                    direction_j = 0
                    direction_i = 0
                elif left == True and right == True:
                    i += direction_i
                    j += direction_j
print(j)

