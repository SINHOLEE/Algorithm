          # 상 하 우 좌
di = [False, -1, 1, 0, 0]
dj = [False, 0, 0, 1, -1]

def change_direction(index):
   global sharkes
   if sharkes[index][3] < 3:
       if sharkes[index][3] == 1:
           sharkes[index][3] = 2
       else:
           sharkes[index][3] = 1
   else:
       if sharkes[index][3] == 3:
           sharkes[index][3] = 4
       else:
           sharkes[index][3] = 3

def catch(num_of_col):
   global R, C, total, sharkes
   cnt = 1000
   my_idx = -1
   for idx_shark in range(len(sharkes)):
       if num_of_col == sharkes[idx_shark][1]:
           if cnt >= sharkes[idx_shark][0]:
               cnt = sharkes[idx_shark][0]
               my_idx = idx_shark
   if my_idx == -1:
       pass
   else:
       a = sharkes.pop(my_idx)
       total += a[4]

def move_sharkes(sharkes):
   global R, C
   dic = {}
   for idx in range(len(sharkes)):
       i = sharkes[idx][0]   # 현재 위치
       j = sharkes[idx][1]   # 현재 위치
       for _ in range(sharkes[idx][2]):  # 속도만큼 움직여라
           i += di[sharkes[idx][3]]
           j += dj[sharkes[idx][3]]
           if i <= 0 or j <= 0 or i > R or j > C:
               change_direction(idx)
               i += di[sharkes[idx][3]] * 2
               j += dj[sharkes[idx][3]] * 2
       if dic.get((i, j)):
           dic[(i, j)].append([sharkes[idx][2], sharkes[idx][3], sharkes[idx][4]])
       else:
           dic[(i, j)] = [[sharkes[idx][2], sharkes[idx][3], sharkes[idx][4]]]
   return dic

def scan(dict1):
   global R, C, sharkes
   new_sharkes = []
   for key, item in dict1.items():
       if len(item) == 1:
           new_sharkes.append([key[0], key[1], item[0][0], item[0][1], item[0][2]])
       else:
           a = sorted(item, key=lambda x:x[-1])[-1]
           new_sharkes.append((key[0], key[1], a[0], a[1], a[2]))
   #
   return new_sharkes

R, C, M = map(int, input().split())
sharkes = []
for m in range(M):
   shark = tuple(map(int, input().split()))  # 좌표i, 좌표j, 속도, 방향, 크기
   sharkes.append(shark)
total = 0
for move in range(1, C + 1):
   catch(move)
   sharkes1 = move_sharkes(sharkes)
   sharkes = scan(sharkes1)
print(total)