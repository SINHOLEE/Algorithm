T = int(input())
def bin_tree(v):
    global i
    if not min_heap[v]:
        i += 1
        my_tree[v] = i
        return
    cnt = 0
    for j in min_heap[v]:
        cnt += 1
        bin_tree(j)
        if cnt == 1:
            i+=1
            my_tree[v] = i
    return
for tc in range(1, T+1):
    n = int(input())
    target = n // 2
    min_heap = [[] for _ in range(1000)]
    idx = 1
    j = 1
    check = False
    for i in range(1, n+1):
        for _ in range(2):
            j+=1
            min_heap[i].append(j)
            if j == n:
                check = True
                break
        if check:
            break

    i = 0
    my_tree = [0] * (n+1)
    bin_tree(1)
    print('#%s %s %s' % (tc, my_tree[1], my_tree[target]))