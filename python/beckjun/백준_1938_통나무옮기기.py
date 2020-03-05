from _collections import deque
'''
너무 하드코딩으로 풀어버렸다... 힘들다..
컨셉은 회전하는 중간좌표만 비짓티드 하고, 나머지는 무시
'''

n = int(input())
mat = [input() for _ in range(n)]

wood = deque([[]])
goal = []
visited = [[[0, 0] for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if mat[i][j] == 'B':
            wood[0].append((i, j))
        if mat[i][j] == 'E':
            goal.append((i, j))

if wood[0][0][0] == wood[0][1][0]:
    wood[0].append(2)  # 가로
else:
    wood[0].append(3)

wood[0].append(0)
visited[wood[0][1][0]][wood[0][1][1]][wood[0][3]-2] = 1
        # 좌    우    하     상
near = [(0, -1), (0, 1), (1, 0), (-1, 0), 'T']
        # d == 2,            d==3
T_map = (((-1, 0), (1, 0)), ((0, -1), (0, 1)))
check = False
while wood:
    one, two, three, d, cnt = wood.popleft()
    w = [one, two, three]

    # 도착지 세 위치가 일치할 때 브레이크
    if goal == w:
        check = True
        break

    for k in range(5):
        # turn
        if near[k] == 'T':
            if visited[two[0]][two[1]][((d-2)+1) % 2] == 1:
                continue
            flag = False
            for i in range(2):
                for ww in w:
                    newX, newY = ww[0]+T_map[d-2][i][0], ww[1] + T_map[d-2][i][1]
                    if not (0 <= newX < n and 0 <= newY < n):
                        flag = True
                        break
                    if mat[newX][newY] == '1':
                        flag = True
                        break
                if flag:
                    break
            if not flag:
                xxx, yyy = two[0], two[1]
                visited[xxx][yyy][((d-2)+1) % 2] = 1
                wood.append(((xxx + T_map[d-2][0][0], yyy + T_map[d-2][0][1]), (xxx, yyy), (xxx + T_map[d-2][1][0], yyy+ T_map[d-2][1][1]), d^1 , cnt + 1))
        else:
            # 4방향으로 이동
            newX, newY = two[0] + near[k][0], two[1] + near[k][1]

            if not (0 <= newX < n and 0 <= newY < n):
                continue
            if visited[newX][newY][d-2]:
                continue

            flag = False
            for www in w:
                newXX, newYY = www[0] + near[k][0], www[1] + near[k][1]
                if not (0 <= newXX < n and 0 <= newYY < n):
                    flag = True
                    break
                if mat[newXX][newYY] == '1':
                    flag = True
                    break
            if not flag:
                visited[newX][newY][d-2] = 1
                wood.append(((one[0] + near[k][0], one[1]+near[k][1]),(newX,newY),(newXX,newYY), d, cnt+1))

if check:
    print(cnt)
else:
    print(0)

