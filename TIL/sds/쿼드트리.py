T = int(input())


def recursion(my_mat, length):
    global res
    mid = length // 2
    maxA = max(sum(my_mat, []))

    A = [[my_mat[i][j] for j in range(0, mid)] for i in range(0, mid)]
    B = [[my_mat[i][j] for j in range(mid, length)] for i in range(0, mid)]
    C = [[my_mat[i][j] for j in range(0, mid)] for i in range(mid, length)]
    D = [[my_mat[i][j] for j in range(mid, length)] for i in range(mid, length)]

    minB = min(max(sum(A, [])), max(sum(B, [])), max(sum(C, [])), max(sum(D, [])))

    if maxA <= 1.2 * minB:
        res += '1'
    else:
        res += '0'
    if length == 4:
        return
    else:
        recursion(A, mid)
        recursion(B, mid)
        recursion(C, mid)
        recursion(D, mid)
        return


for t in range(1, T+1):
    temp = [*map(int,input().strip().split())]
    n = temp.pop(0)
    mat = []
    for i in range(n):
        mat.append(temp[n*i:n*(i+1)])

    res = ''

    recursion([arr[:] for arr in mat], n)
    print('#%s %s' % (t, res))

