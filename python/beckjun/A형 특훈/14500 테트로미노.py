'''
조건을 제대로 안읽으면 생기는 불상사.
숨겨져 있는 조건을 잘 읽어라
이문제에서는 좌우 대칭이가능하다는 부분을 간과해서 대칭의 경우를 생각하지 않아 틀린문제.
로직은 간단하다.
상우하좌를 응용해서 시계방향으로 돌리는 로직을 각 (인덱스 +1) % 4 로 구현했고,
대각선 으로 이동은 두 벡터를 시계방향으로 이동한 후 두 벡터를 합치는 것으로 표현가능하다.
'''

n, m = map(int, input().split())

def is_wall(x, y):
    if x< 0 or x> n-1 or y < 0 or y > m-1:
        return True
    return False

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
score_mat = [ list(map(int, input().split())) for _ in range(n)]


# ㄹ자
def fn(x, y,num):
    global max_val
    if num == 0: # 리을
        my_track = [1, 0, 1]
        kk = 2
    elif num == 1: # 일자
        my_track = [1, 1, 1]
        kk = 2
    elif num == 2:  # 사각
        my_track = [1, 2, 3]
        kk = 1
    elif num == 3:
        my_track = [2, 2, 1]
        kk = 4
    elif num == 4:
        my_track = [1, 2, 1]
        kk = 2

    elif num == 5:
        my_track = [2, 2, 3]
        kk = 4
    else:
        my_track = [1,1,2,3] # 2, 3번 인덱스는 합쳐야 한다.
        kkk = 4
        start = score_mat[x][y]
        start_x = x
        start_y = y
        res = start
        for i in range(kkk):
            x = start_x
            y = start_y
            res = start
            flag = False
            for k in range(len(my_track)-1):
                if k ==2:
                    x = x +di[(my_track[k]+i) % 4] + di[(my_track[k+1]+i) % 4]
                    y = y + dj[(my_track[k] + i) % 4] + dj[(my_track[k+1] + i) % 4]
                else:
                    x = x + di[(my_track[k] + i) % 4]
                    y = y + dj[(my_track[k] + i) % 4]
                if is_wall(x, y):
                    res = start
                    flag = True
                    break
                res += score_mat[x][y]

            if not flag:
                if max_val < res:
                    max_val = res

        return

    start = score_mat[x][y]
    start_x = x
    start_y = y
    res = start
    for i in range(kk):
        x = start_x
        y = start_y
        res = start
        flag = False
        for k in my_track:
            x = x + di[(k + i) % 4]
            y = y + dj[(k+i) % 4]
            if is_wall(x, y):
                res = start
                flag = True
                break
            res += score_mat[x][y]
        if not flag:
            if max_val < res:
                max_val = res
    return


max_val = 0


for i in range(n):
    for j in range(m):
        for z in range(7):
            fn(i, j, z)

print(max_val)


