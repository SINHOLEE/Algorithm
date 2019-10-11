T = int(input())
for tc in range(1, T+1):
    n, m, l = map(int, input().split())
    my_tree = [-1] * (n+1)
    parent2child = [[] for _ in range(n+1)]

    idx = 1
    check = False
    for i in range(1, n+1):
        for j in range(2):
            idx += 1
            parent2child[i].append(idx)
            if idx == n:
                check = True
                break
        if check:
            break

    for k in range(m):
        node, digit = map(int, input().split())
        my_tree[node] = digit

    for i in range(n-1, -1, -1):
        if my_tree[i] != -1:
            continue
        my_sum = 0
        for item in parent2child[i]:
            my_sum += my_tree[item]
        my_tree[i] = my_sum
    print('#%s %s' % (tc, my_tree[l]))