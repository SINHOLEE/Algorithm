T = int(input())

for tc in range(1, T+1):
    n = int(input())
    tree = [0] * (n+1)
    my_list = list(map(int, input().split()))
    for ii in range(1, n+1):
        tree[ii] = my_list[ii-1]
        while True:
            if tree[ii] > tree[ii // 2]:
                break
            tree[ii], tree[ii // 2] = tree[ii // 2], tree[ii]
            ii = ii // 2

    res = 0
    while True:
        if n < 1:
            break
        n = n // 2
        res += tree[n]
    print("#%s %s" % (tc, res))