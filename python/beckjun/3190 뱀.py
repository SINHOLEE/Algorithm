    # 시계방향 (D면 +1, L이면 -1)
    # 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
n = int(input())

k = int(input())

apples = set()
for _ in range(k):
    i, j = map(int, input().split())
    apples.add((i-1, j-1))

l = int(input())


direction = []
cnt = 0
for _ in range(l):
    temp = list(map(str, input().split()))

    direction.append([int(temp[0]) - cnt, temp[1]])
    cnt = int(temp[0])

pointer = 0  # 첫 시작은 우측으로 시작.
time = 0

i = 0
j = 0
body = [(0, 0)]
count = 0
while True:
    count += 1
    time += 1
    i += di[pointer]
    j += dj[pointer]

    # 종료조건
    if i < 0 or i > n - 1 or j < 0 or j > n - 1 or (i, j) in body:
        break
    body.append((i, j))
    # 사과 먹거나 안먹을 때 움직임
    if (i, j) in apples:
        apples.remove((i,j))
    else:
        body.pop(0)
    # 방향전환 로직
    if len(direction) != 0:
        direction[0][0] -= 1
    if  len(direction) != 0  and direction[0][0] == 0:
        if direction[0][1] == 'D':
            pointer = (pointer + 1) % 4
        else:
            if pointer == 0:
                pointer = 3
            else:
                pointer = (pointer - 1) % 4
        if len(direction) == 1:
            direction = []
        else:
            direction = direction[1:]

print(time)