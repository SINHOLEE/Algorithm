def bin_search(l, r, target):
    global count, N, check, first

    mid = (l + r) // 2

    if a_list[mid] == target:
        count += 1
        first = True
        return

    if first:
        if target < a_list[mid]:
            check = 0
        else:
            check = 1
        first = False

    if target < a_list[mid] and check == 0:
        check += 1
        bin_search(l, mid - 1, target)
        return
    if target > a_list[mid] and check == 1:
        check -= 1
        bin_search(mid + 1, r, target)
        return


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    a_list = sorted(list(map(int, input().split())))
    b_list = list(map(int, input().split()))
    count = 0
    check = 0

    for target1 in range(M):
        first = True

        if a_list[N - 1] < b_list[target1]:
            continue
        bin_search(0, N - 1, b_list[target1])

    print('#%s %s' % (tc, count))

