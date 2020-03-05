from pprint import pprint

def count_color_mat(mat):
    for i in range(N):
        for j in range(M):
            color_count[mat[i][j]] += 1

    return max(color_count)

def paint(x1, y1, x2, y2, color):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            mat[i][j] = color

def check_paint(x1, y1, x2, y2, color):
    # 만약 이 범위 안에 color보다 작거나 같으면 패인팅 해도 된다. = True
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if mat[i][j] <= color:
                pass
            else:
                return False
    return True


T = int(input())

for tc in range(1, T+1):
    # N은 행의 개수, M은 열의 개수, K는 패인트의 개수
    N, M, K = map(int, input().split())
    mat = [[0] * M for _ in range(N)]
    color_count = [0] * 11

    for k in range(K):
        # x1, y1 좌측상단, x2, y2 우측하단
        x1, y1, x2, y2, color = map(int, input().split())
        if check_paint(x1, y1, x2, y2, color):
            paint(x1, y1, x2, y2, color)

    print('#{} {}'.format(tc, count_color_mat(mat)))





