from _collections import deque
n = int(input())

mat = [input() for _ in range(n)]

wood = deque([[]])
goal = []
visited = [[[0,0] for _ in range(n)] for _ in range(n)]

print(visited)
for i in range(n):
    for j in range(n):
        if mat[i][j] == 'B':
            wood[0].append((i,j))
        if mat[i][j] == 'E':
            goal.append((i,j))


if wood[0][0][0] == wood[0][1][0]:
    wood[0].append(3) #가로
else:
    wood[0].append(4)

if goal[0][0] == goal[1][0]:
    goal.append(3)
else:
    goal.append(4)
wood[0].append(0)

print(wood)
print(goal)
visited[wood[0][1][0]][wood[0][1][1]][wood[0][3]-3] = 1

for a in visited:
    print(a)
        # 좌    우    하     상
near = [(0,-1),(0,1),(1,0),(-1,0),'T']
T_map = (-1, 1)
while wood:
    one, two, three, d, cnt = wood.popleft()
    w = [one, two, three]

    for n in range(5):
        if near[n] == 'T':
            # turn
            if d == 3:
                if visited[two[0]][two[1]] == 3:
                    continue
                for i in range(2):
                    for ww in w:
                        newX, newY = ww[0]+T_map[i], ww[1]

        else:
            pass

