from pprint import pprint

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    mat = [[0] * (v+1) for _ in range(v+1)]
    for _ in range(e):
        i, j, w = map(int, input().split())
        mat[i][j] = w
        mat[j][i] = w
    # pprint(mat)
    key = [99999] * (v+1)
    pi = [0] * (v+1)
    vistied = [False] * (v+1)

    min_sum_w = 9999999
    count = 0
    my_sum = 0
    node = 0
    while True:
        vistied[node] = True
        count += 1
        if count == v+1:
            if min_sum_w > my_sum:
                min_sum_w = my_sum
            break
        if min_sum_w < my_sum:
            break
        for next in range(len(mat[node])):
            if mat[node][next] != 0:
                if key[next] > mat[node][next] and vistied[next] == False: # visited  빼도 되는지 모름
                    key[next] = mat[node][next]
                    pi[next] = node

        min_idx = -1
        min_w = 9999999
        for w in range(len(key)):
            if min_w > key[w] and vistied[w] == False:
                min_idx = w
                min_w = key[w]
        my_sum += min_w
        node = min_idx

    print('#%s %s' % (tc, min_sum_w))
