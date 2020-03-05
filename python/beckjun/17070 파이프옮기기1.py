from pprint import pprint

def move(i, j, direction_status):
    global count, N, cnt
    cnt += 1
    if (i, j) == (N-1, N-1):
        count += 1
        return

    if direction_status == 0:  # 이전에 가로일 때
        if j+1 > N-1 or mat[i][j+1] == 1:  # 오른쪽으로 이동할 때 방해하는게 있으면 패스
            pass
        else:  # 오른쪽으로 이동할 때 방해하는게 없으면 무브
            move(i, j+1, 0)
        if i+1 > N-1 or j+1 > N-1 or mat[i][j+1] == 1 or mat[i+1][j+1] == 1 or mat[i+1][j] == 1:
            # 대각선 밑으로 움직일 때 방해가 있으면 패스
            pass
        else:  # 방해가 없으면 무브
            move(i+1, j+1, 2)
    elif direction_status == 1:  # 이전이 세로일 때
        if i+1 > N-1 or mat[i+1][j] == 1:  # 아래로 이동할 때 방해하는게 있으면 패스
            pass
        else:  # 아래로 이동할 때 방해하는게 없으면 무브
            move(i+1, j, 1)
        if i+1 > N-1 or j+1 > N-1 or mat[i][j+1] == 1 or mat[i+1][j+1] == 1 or mat[i+1][j] == 1:
            # 대각선으로 움직일 때 방해가 있으면 패스
            pass
        else:  # 방해가 없으면 무브
            move(i+1, j+1, 2)

    else:  # 이전이 대각선일 때
        if i+1 > N-1 or mat[i+1][j] == 1:  # 아래로 이동할 때 방해하는게 있으면 패스
            pass
        else:  # 아래로 이동할 때 방해하는게 없으면 무브
            move(i+1, j, 1)
        if i+1 > N-1 or j+1 > N-1 or mat[i][j+1] == 1 or mat[i+1][j+1] == 1 or mat[i+1][j] == 1:
            # 대각선으로 움직일 때 방해가 있으면 패스
            pass
        else:  # 방해가 없으면 무브
            move(i+1, j+1, 2)
        if j+1 > N-1 or mat[i][j+1] == 1:  # 오른쪽으로 이동할 때 방해하는게 있으면 패스
            pass
        else:  # 오른쪽으로 이동할 때 방해하는게 없으면 무브
            move(i, j+1, 0)


N = int(input())
mat = [list(map(int, input().split())) for i in range(N)]
head_i = 0
head_j = 1
count = 0         #가로 세로 대각선
cnt = 0
# direction_status = [0, 1, 2]
move(head_i, head_j, 0)
print(count)