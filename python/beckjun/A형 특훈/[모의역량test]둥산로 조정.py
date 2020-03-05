'''
디버깅을 이런식으로 하니 한눈에 보기 좋다.

'''
T = int(input())
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
DEBUG = False

def move(x, y, length, done, mat, now_val):
    global max_res
    if DEBUG:
        print(length)
        print(x, y, done)
        for i in range(N):
            for j in range(N):
                print(mat[i][j], end=' ')
            print()
        print()
        for i in range(N):
            for j in range(N):
                print(visited[i][j], end=' ')
            print()


    for k in range(4):
        if  not (0 > x+di[k] or N-1 < x+di[k] or 0 > y+dj[k] or N-1 < y+dj[k]):
            if visited[x + di[k]][y + dj[k]] == 0 and mat[x+di[k]][y+dj[k]] < now_val:
                visited[x + di[k]][y + dj[k]] = 1
                move(x + di[k], y + dj[k], length + 1, done, [arr[:] for arr in mat], mat[x+di[k]][y+dj[k]])
                visited[x + di[k]][y + dj[k]] = 0
            else:
                if max_res < length:
                    max_res = length

        else:
            if max_res < length:
                max_res = length

        if done == False:
            if  not (0 > x+di[k] or N-1 < x+di[k] or 0 > y+dj[k] or N-1 < y+dj[k]):
                for decrease in range(1, K+1):
                    if visited[x+di[k]][y+dj[k]] == 0 and mat[x+di[k]][y+dj[k]] - decrease < now_val:
                        mat[x+di[k]][y+dj[k]] -= decrease
                        visited[x+di[k]][y+dj[k]] = 1
                        move(x+di[k], y+dj[k], length + 1, True, [arr[:] for arr in mat], mat[x+di[k]][y+dj[k]])
                        mat[x+di[k]][y+dj[k]] += decrease
                        visited[x + di[k]][y + dj[k]] = 0
            else:
                if max_res <length:
                    max_res = length



for t in range(1, T+1):
    N, K = map(int, input().split())
    mat = []
    max_list = []
    max_val = 0
    for i in range(N):
        temp = []
        input_data = list(map(int, input().split()))
        for j in range(N):
            if max_val < input_data[j]:
                max_val = input_data[j]
                max_list = [(i, j)]
            elif max_val == input_data[j]:
                max_list.append((i, j))
            temp.append(input_data[j])
        mat.append(temp)
    max_res = 0
    visited = [[0] * N for _ in range(N)]
    for x, y in max_list:
        visited[x][y] = 1
        move(x, y, 1, False, [arr[:] for arr in mat], max_val )
        visited[x][y] = 0

    print('#%s %s' % (t, max_res))