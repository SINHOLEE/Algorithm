n, m, k = map(int, input().split())
    # 위 아래 왼 오른
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

mat = [ [*map(int, input().split())] for _ in range(n)]
smell_mat = [[[0, 0] for _ in range(n)] for _ in range(n)]  # 상어번호, 냄새 남은 횟수
sharks = [[] for _ in range(m+1)]

for i in range(n):
    for j in range(n):
        if mat[i][j]:
            sharks[mat[i][j]] = [i, j]
            smell_mat[i][j] = [mat[i][j], k]

directions = list(map(int, input().split()))

for idx in range(1, m+1):
    sharks[idx].append(directions[idx-1]-1)



directions_order = [[] for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(4):
        temp = list(map(lambda x:int(x)-1, input().split()))
        directions_order[i].append(temp)


# 전처리 끝, 상어 시뮬레이션 시작.
for rnd in range(1, 1001):  # 1000번의 시뮬레이션
    # 2. 상어이동
    for shark_idx in range(1, m+1):
        if not sharks[shark_idx]:
            continue
        y, x, d = sharks[shark_idx]

        for kk in directions_order[shark_idx][d]:
            ny, nx = y + dy[kk], x+dx[kk]
            if not (0 <= ny < n and 0 <= nx < n):
                continue
            if smell_mat[ny][nx][1] == k+1:
                mat[y][x] = 0  # 퇴출 당함
                sharks[shark_idx] = []  # 퇴출당함
                break
            if smell_mat[ny][nx][1] == 0:  # 0일 때,
                mat[y][x] = 0
                mat[ny][nx] = shark_idx
                sharks[shark_idx] = [ny, nx, kk]  # 방향전환
                smell_mat[ny][nx] = [shark_idx, k+1]
                break
        else:
            for kk in directions_order[shark_idx][d]:
                ny, nx = y+dy[kk], x+dx[kk]
                if not (0 <= ny < n and 0 <= nx < n):
                    continue
                if smell_mat[ny][nx][0] == shark_idx:
                    mat[y][x] = 0
                    mat[ny][nx] = shark_idx
                    sharks[shark_idx] = [ny, nx, kk]
                    smell_mat[ny][nx] = [shark_idx, k+1]
                    break

    # 1. 냄새 감가상각
    for i in range(n):
        for j in range(n):
            if smell_mat[i][j][1] > 1:
                smell_mat[i][j][1] -= 1
            elif smell_mat[i][j][1] == 1:
                smell_mat[i][j] = [0, 0]

    # 3. 상어 한마리만 남았나?
    cnt = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j]:
                cnt+=1
    if cnt == 1:
        print(rnd)
        break
else:
    print(-1)

