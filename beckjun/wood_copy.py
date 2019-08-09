from pprint import pprint

global woods
woods = []
global grave
grave = []

def wood_sort(woods):

    for i in range(len(woods)-1):
        min_age = 100000000
        min_index = 0
        for j in range(i, len(woods)):
            if min_age > woods[j][2]:
                min_age = woods[j][2]
                min_index = j
        woods[i], woods[min_index] = woods[min_index], woods[i]
    return woods



def isout(r, c, N):
    if 0 <= r and N-1 >= r and 0 <= c and N-1 >= c:
        return False
    else:
        return True


N, M, K = input().split()
N, M, K = int(N), int(M), int(K)

ground = []
for i in range(N):
    temp = [5] * N
    ground.append(temp)

winter_add = []
for n in range(N):
    temp = list(map(int, input().split()))

    winter_add += [temp]


for m in range(M):
    wood = list(map(int, input().split()))
    for w in range(len(wood)):
        if w == 0 or w == 1:
            wood[w] -= 1
    woods += [wood]


dr = [ -1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for k in range(K):
    temp_woods = wood_sort(woods)
    temp = []
    for wood in range(len(temp_woods)):

        if ground[temp_woods[wood][0]][temp_woods[wood][1]] < temp_woods[wood][2]:  # 만약 나이보다 양분이 부족하다면
            dead = temp_woods[wood]
            temp.append(wood)
            grave.append(dead)
        else:
            ground[temp_woods[wood][0]][temp_woods[wood][1]] -= temp_woods[wood][2]
            woods[wood][2] += 1
    if len(temp) != 0:
        for tt in range(len(temp)):
            temp_woods.pop(temp[tt]-tt)

    woods = temp_woods


    if len(grave) >= 1:
        for g in range(len(grave)):
            ground[grave[g][0]][grave[g][1]] += grave[g][2] // 2


    for wood in range(len(woods)):

        if woods[wood][2] % 5 == 0:  # 나이가 3이라면
            for direction in range(8):

                if isout(woods[wood][0] + dr[direction], woods[wood][1] + dc[direction], N):
                    pass  # 방향이 바깥이면 패스하고 바깥이 아니면 나무를 생성하라!
                else:
                    temp = [woods[wood][0] + dr[direction], woods[wood][1] + dc[direction], 1]
                    # print(temp)
                    woods.append(temp)
                    temp = []


    for i in range(N):
        for j in range(N):
            ground[i][j] += winter_add[i][j]





print(len(woods))
