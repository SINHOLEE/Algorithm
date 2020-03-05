import sys
import heapq
input = sys.stdin.readline

di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]

N, M, K = map(int, input().split())

mat = [[5] * N for _ in range(N)]

A = [list(map(int, input().split())) for _ in range(N)]

# my_data[x][y][0] == deque, my_data[x][y][1] == dead_trees
my_data = [[[[], []] for _ in range(N)] for _ in range(N)] # 여기에 dequeue로 만든 trees 와 dead_trees 배열을 관리한다.

for m in range(M):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    heapq.heappush(my_data[x][y][0], z * -1)



for _ in range(K): # k년 만큼 반복한다.
    # 여름
    for i in range(N):
        for j in range(N):
            new_heapq = []
            # 3차원 배열 안에서 부터 시작한다.
            while True:
                if len(my_data[i][j][0]) == 0:
                    break
                age = my_data[i][j][0].pop()
                age = -1 * age


                if age <= mat[i][j]:
                    mat[i][j] -= age
                    age += 1
                    heapq.heappush(new_heapq, age * -1)
                else:
                    my_data[i][j][1].append(age)
            my_data[i][j][0] = new_heapq

    # 여름 가을 겨울
    for i in range(N):
        for j in range(N):
            # 여름
            while True:
                # dead_trees
                if len(my_data[i][j][1]) == 0:
                    break
                age = my_data[i][j][1].pop()
                mat[i][j] += age // 2
            # 가을
            for item_age in my_data[i][j][0]:
                item_age = -1 * item_age
                if item_age % 5 == 0:
                    for k in range(8):
                        if i+di[k] < 0 or i+di[k] > N-1 or j + dj[k] < 0 or j + dj[k] > N - 1:
                            continue
                        heapq.heappush(my_data[i+di[k]][j + dj[k]][0], -1)

            # 겨울
            mat[i][j] += A[i][j]

res = 0
for i in range(N):
    for j in range(N):
        cnt = len(my_data[i][j][0])
        res += cnt
print(res)