'''
조건에 부합하게 짯다.
디테일한 부분에서 디버깅을 하지 못하면 아직 한번에 완벽한 코드로 구현하지 못한다.
'''

n, l = map(int,input().split())

mat = [list(map(int, input().split())) for i in range(n)]
visited_dummy = [[0] * n for _ in range(n)]

total = 0
for i in range(n):
    check = False
    j = 0
    # 좌에서 우로
    cur_height = mat[i][j]
    visited = [arr[:] for arr in visited_dummy]
    while True:
        if j > n-1:
            # 끝까지 무사히 갔다면 total +=1
            total += 1
            break
        if j+1 < n and mat[i][j+1] == cur_height:
           pass
        else:
            # 현재 위치의 높이보다 갈 곳이 1 높다면
            if j+1 < n and mat[i][j+1] - cur_height == 1:
                for back in range(l):  # 현재위치부터 l거리까지  모든 경우에서 왼쪽으로 인덱스가 바깥이 아니고, 현재위치의 높이와 같으며, 한번도 경사로를 설치하지 않은 공간이라면 설치하고 지나가도 된다.
                    if j-back >= 0 and mat[i][j-back] == cur_height and visited[i][j - back] == False:
                        continue
                    else:
                        check = True
                        break
                if check == False:
                    for back in range(l):
                        visited[i][j - back] = True
                    j += 1
                    cur_height = mat[i][j]
                    continue
            # 현재 위치의 높이보다 갈 곳이 1 낮다면
            elif j+1 < n and cur_height - mat[i][j+1] == 1:
                for front in range(1,l+1):
                    if j+front < n and mat[i][j+front] == cur_height - 1 and visited[i][j+front] == False:
                        continue
                    else:
                        check = True
                        break
                if check == False:
                    for front in range(1, l+1):
                        visited[i][j+front] = True
                    j += l
                    cur_height = mat[i][j]
                    continue
            else:
                if j >= n-1:
                    total += 1
                break

        # 중간에 멈춘다면 다음 순서로 간다.
        if check:
            break
        j += 1

    # -------- 반대로
    check = False
    j = 0
    # 위에서 아래로
    cur_height = mat[j][i]
    visited = [arr[:] for arr in visited_dummy]
    while True:
        if j > n - 1:
            # 끝까지 무사히 갔다면 total +=1
            total += 1
            break
        if j + 1 < n and mat[j+1][i] == cur_height:
            pass
        else:
            # 현재 위치의 높이보다 갈 곳이 1 높다면
            if j + 1 < n and mat[j+1][i] - cur_height == 1:
                for back in range(
                        l):  # 현재위치부터 l거리까지  모든 경우에서 왼쪽으로 인덱스가 바깥이 아니고, 현재위치의 높이와 같으며, 한번도 경사로를 설치하지 않은 공간이라면 설치하고 지나가도 된다.
                    if j - back >= 0 and mat[j-back][i] == cur_height and visited[j-back][i] == False:
                        continue
                    else:
                        check = True
                        break
                if check == False:
                    for back in range(l):
                        visited[j-back][i] = True
                    j += 1
                    cur_height = mat[j][i]
                    continue
            # 현재 위치의 높이보다 갈 곳이 1 낮다면
            elif j + 1 < n and cur_height - mat[j+1][i] == 1:
                for front in range(1, l + 1):
                    if j + front < n and mat[j + front][i] == cur_height - 1 and visited[j + front][i] == False:
                        continue
                    else:
                        check = True
                        break
                if check == False:
                    for front in range(1, l + 1):
                        visited[j + front][i] = True
                    j += l
                    cur_height = mat[j][i]
                    continue
            else:
                if j >= n - 1:
                    total += 1
                break

        # 중간에 멈춘다면 다음 순서로 간다.
        if check:
            break
        j += 1

print(total)