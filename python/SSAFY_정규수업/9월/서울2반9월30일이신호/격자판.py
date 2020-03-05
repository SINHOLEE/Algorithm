T = int(input())

def DFS(depth, lis , i, j):
    if depth == 7:
        lis = tuple(lis)
        my_set.add(lis)
        return
    # 상
    if i-1 >= 0:
        DFS(depth+1, lis + [mat[i-1][j]], i-1, j)
    # 하
    if i+1 <= 3:
        DFS(depth+1, lis + [mat[i+1][j]], i+1, j)
    # 좌
    if j-1 >= 0:
        DFS(depth+1, lis + [mat[i][j-1]], i, j-1)
    # 우
    if j+1 <= 3:
        DFS(depth+1, lis + [mat[i][j+1]], i, j+1)


for tc in range(1, T+1):
    mat = [list(map(int, input().split())) for _ in range(4)]

    my_set = set()

    for ii in range(4):
        for jj in range(4):
            my_list = []
            DFS(1, my_list + [mat[ii][jj]], ii, jj)
    count = 0
    for item in my_set:
        count+=1
    print('#%s %s' % (tc, count))
