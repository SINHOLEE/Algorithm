dic = { 'U': (-1, 0, 0),
        'D': (1, 0, 1),
        'L': (0, -1, 2),
        'R': (0, 1, 3)
}


def solution(dirs):
    mat = [[[0, 0,0 ,0] for _ in range(11)] for _ in range(11)]
    y , x = 5, 5
    res = 0
    for dir in dirs:
        ny, nx = y+dic[dir][0], x+dic[dir][1]
        if not (0<=ny<11 and 0<=nx<11):
            continue
        if mat[ny][nx][dic[dir][2]] == 0 and mat[y][x][(dic[dir][2])^1] == 0:
            mat[ny][nx][dic[dir][2]] = 1
            res += 1
        y=ny
        x=nx
    return res


solution('ULURRDLLU')
