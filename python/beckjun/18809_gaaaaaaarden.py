from _collections import deque


def bfs():
    global visited_list, injectable_area, mat, n, m, res, visited_mat
    for i in range(n):
        for j in range(m):
            visited_mat[i][j][0] = 0
            visited_mat[i][j][1] = 0
    flower_cnt = 0
    q = deque([])
    for i in range(len(visited_list)):
        if visited_list[i]:
            y = injectable_area[i][0]
            x = injectable_area[i][1]
            visited_mat[y][x][0] = visited_list[i]
            q.append((y, x, visited_list[i], 0))

    while q:
        y, x, color, cnt = q.popleft()
        # 꽃이 됐으면 진행하지 말아라
        if visited_mat[y][x][0] == 9:
            continue
        for k in range(4):
            ny, nx = y+dy[k], x+dx[k]
            # 그리드 밖이 아니다.
            if not(0 <= ny < n and 0 <= nx < m):
                continue
            # 호수가 아니다
            if mat[ny][nx] == 0:
                continue
            # 이미 배양액이 없다면,
            if visited_mat[ny][nx][0] == 0:
                visited_mat[ny][nx][0] = color
                visited_mat[ny][nx][1] = cnt + 1
                q.append((ny, nx, color, cnt+1))
            else:  # 이미 배양액이 있다면,
                if visited_mat[ny][nx][0] == color ^ 1 and visited_mat[ny][nx][1] == cnt+1:
                    flower_cnt += 1  # 꽃을 하나 증가시키고
                    visited_mat[ny][nx][0] = 9  # 그 위치를 꽃으로 표시해서 다음 번 해당 위치의 배양액이 다음 로직을 수행하지 않도록 preventEvent 한다.

    return flower_cnt


# [0,0,0,0,0,0,0,0,0] , g = 4, r = 3 일 경우, [g,g,g,g,r,r,r,0,0,0] 과 같은 조합을 구해야 하므로,
#  1. 녹색배양액의 위치를 먼저 선점한 뒤, 2. 빨간 배양액의 위치를 조합의 경우로 구해 bfs 시작지점을 설정한다.
def combi(curr_idx, curr_cnt, target, target_cnt):
    global visited_list, g, r, res

    if curr_cnt == target_cnt:
        if target == 3:  # 현재 빨간 배양액을 바라보고 있으면, 종료
            # 2. 시뮬레이션 시작.
            res = max(res, bfs())
        else:  # 현재 그린배양액을 바라보고 있으면,
            combi(0, 0, 3, r)  # 빨간 배양액 위치 찾기
        return

    for j in range(curr_idx, len(visited_list)):
        if visited_list[j]:
            continue
        visited_list[j] = target
        combi(j, curr_cnt+1, target, target_cnt)
        visited_list[j] = 0


n, m, g, r = map(int, input().split())
res = 0
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
mat = [[*map(int, input().split())] for _ in range(n)]
injectable_area = []
for i in range(n):
    for j in range(m):
        if mat[i][j] == 2:
            injectable_area.append((i, j))
# 1. 배양 가능한 좌표 구하기 g == 2, r == 3
visited_list = [0] * len(injectable_area)
# idx 0 == 배양색깔 표시, idx 1 == 해당위치에 도착하기 까지 걸린 시간 == cnt
visited_mat = [[[0, 0] for _ in range(m)] for _ in range(n)]
combi(0, 0, 2, g)  # 녹색 배양액 위치 정하기
print(res)


