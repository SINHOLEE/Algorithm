def move(y, x, d, mat, n):
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    sand_spead = [
        {
        'start_y': 2,
        'start_x' : 3,
        'board' : [
            [0, 0, 0.02, 0, 0],
            [0, 0.1, 0.07, 0.01, 0],
            [0.05, 0, 0, 0, 0],
            [0, 0.1, 0.07, 0.01, 0],
            [0, 0, 0.02, 0, 0]
            ]
        },
        {
        'start_y': 1,
        'start_x' : 2,
        'board' : [
            [0, 0, 0, 0, 0],
            [0, 0.01, 0, 0.01, 0],
            [0.02, 0.07, 0, 0.07, 0.02],
            [0, 0.1, 0, 0.1, 0],
            [0, 0, 0.05, 0, 0]
            ]
        },
        {
        'start_y': 2,
        'start_x' : 1,
        'board' : [
            [0, 0, 0.02, 0, 0],
            [0, 0.01, 0.07, 0.1, 0],
            [0, 0, 0, 0, 0.05],
            [0, 0.01, 0.07, 0.1, 0],
            [0, 0, 0.02, 0, 0]
            ]
        },
        {
        'start_y': 3,
        'start_x' : 2,
        'board' : [
            [0, 0, 0.05, 0, 0],
            [0, 0.1, 0, 0.1, 0],
            [0.02, 0.07, 0, 0.07, 0.02],
            [0, 0.01, 0, 0.01, 0],
            [0, 0, 0, 0, 0]
            ]
        },
    ]  
    out_bound_sand = 0
    start_y, start_x = sand_spead[d]['start_y'], sand_spead[d]['start_x']
    board = sand_spead[d]['board']
    target_y, target_x = y+dy[d], x+dx[d]
    a_y, a_x = y+2*dy[d], x+2*dx[d]
    target_sand = mat[target_y][target_x]
    a_sand = target_sand # 이제 모든 mat들의 가중치를 곱해서 뺀값이 a먼지 양이다. 
    for i in range(5):
        for j in range(5):
            adj_y = i-start_y
            adj_x = j-start_x
            ny, nx = y+adj_y, x+adj_x
            
            moved_sand = int(target_sand * board[i][j])
            mat[target_y][target_x] -= moved_sand
            a_sand -= moved_sand
            if not (0<=ny<n and 0<=nx<n):
                out_bound_sand += moved_sand
            else:
                mat[ny][nx] += moved_sand
    mat[target_y][target_x] -= a_sand
    if not (0<=a_y<n and 0<=a_x<n):
        out_bound_sand += a_sand
    else:
        mat[a_y][a_x] += a_sand
    return mat, out_bound_sand

def solution(n, mat):
    #   좌 하 우 상
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    y = n // 2
    x = n // 2
    d = 0
    res = 0
    for cnt in range(1, n):
        for _ in range(2):
            for _ in range(cnt):
                ny, nx = y+dy[d], x+dx[d]
                mat[y][x] = d
                mat, out_bound_sand = move(y,x,d,mat,n)
                res += out_bound_sand
                y, x = ny, nx
            d = (d+1) % 4
    
    for _ in range(1, n):
        ny, nx = y+dy[d], x+dx[d]
        mat, out_bound_sand = move(y,x,d,mat,n)
        res += out_bound_sand
        y, x = ny, nx
    return res
# if __name__ == "__main__":
n = int(input())
mat = [[*map(int, input().split())] for _ in range(n)]

print(solution(n, mat))