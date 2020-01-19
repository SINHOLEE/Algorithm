T = int(input())

for t in range(T):
    n = int(input())
    frist_rev_test = [0] * (n+1)
    second_rev_test = [0] * (n+1)
    first_test = [0] * (n+1)
    second_test = [0] * (n+1)
    for i in range(1, n+1):
        a, b = map(int, input().split())
        frist_rev_test[i] = a
        second_rev_test[i] = b
        first_test[a] = i
        second_test[b] = i
        if a == 1:
            first_num_one = i
        if b == 1:
            second_num_one = i
        if a == n:

            first_last_one = i
        if b == n:
            second_last_one = i
    print(first_test)
    print(second_test)
    print(frist_rev_test)
    print(second_rev_test)
    cnt = 0
    aa = second_rev_test[first_last_one]
    bb = second_rev_test[second_last_one]
    for i in range(1, first_test.index(second_num_one)+1):
        if first_test[i] == first_num_one or first_test[i] == second_num_one:
            cnt += 1

        elif aa > second_rev_test[first_test[i]] and bb > second_rev_test[first_test[i]]:
            cnt += 1
    print(cnt)
