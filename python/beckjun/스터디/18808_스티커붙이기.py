def turn_90(sticker):
    r = len(sticker)
    c = len(sticker[0])
    new_sticker = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            new_sticker[j][r-1-i] = sticker[i][j]
    return new_sticker


def locate(sticker1, notebook1):
    global n, m, sticker_n, sticker_m
    for i in range(n-sticker_n+1):
        for j in range(m-sticker_m+1):
            # 만약 체크했을 때 참이면
            # 그 참인 대로의 노트북을 리턴하라
            if check(i, j, notebook1, sticker1):
                return True
    return False


def check(i, j, notebook2, sticker2):
    global sticker_n, sticker_m
    for ii in range(sticker_n):
        for jj in range(sticker_m):
            if notebook2[ii+i][jj+j] == 1:
                if sticker2[ii][jj] == 1:
                    return False
    for ii in range(sticker_n):
        for jj in range(sticker_m):
            if sticker2[ii][jj] == 1:
                notebook2[ii+i][jj+j] = 1

    return True


n, m, k = map(int, input().split())
notebook = [[0] * m for _ in range(n)]
stickers = []
for _ in range(k):
    r, c = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(r)]
    stickers.append(mat)

for _ in range(k):
    # 회전하는 로직
    temp_sticker = stickers[_] ## 인자를 _와 sticker로 받아서 회전된 스티커를 반환하자
    sticker_n = len(temp_sticker)
    sticker_m = len(temp_sticker[0])
    for kk in range(4):
        # 한번 회전하면 그 회전한 스티커 모양으로 노트북을 순회해
        if kk > 0:
            temp_sticker = turn_90(temp_sticker)
            sticker_n, sticker_m = sticker_m, sticker_n
        # 일단 회전된 스티커가 노트북 크기보다 작은지 체크
        if n < sticker_n or m < sticker_m:
            continue
        flag = locate(temp_sticker, notebook)
        if flag:
            break
print(sum(sum(notebook,[])))
