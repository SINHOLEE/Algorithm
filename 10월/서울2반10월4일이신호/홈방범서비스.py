def make_k_ij(k):
    if k == 1:
        k_bucket[k] = [(0, 0)]
        return
    else:
        my_list = k_bucket[k - 1][:]
        i = my_list[-1][0]  # 우측에서 시작
        j = my_list[-1][1] + 1

        count = 0
        while True:  # 하
            if count == k - 1:
                break
            i += 1
            j -= 1
            my_list.append((i, j))
            count += 1
        count = 0

        while True:  # 좌
            if count == k - 1:
                break
            i -= 1
            j -= 1
            my_list.append((i, j))
            count += 1
        count = 0

        while True:  # 상
            if count == k - 1:
                break
            i -= 1
            j += 1
            my_list.append((i, j))
            count += 1
        count = 0

        while True:  # 우
            if count == k - 1:
                break
            i += 1
            j += 1
            my_list.append((i, j))
            count += 1
        k_bucket[k] = my_list
        return


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]

    nums_of_home = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j]:
                nums_of_home += 1

    ans_count = 0
    k_bucket = {}
    for k in range(1, 46):  # 50이 k를 만들때 방범비용이 가장 크면서 n**2 *m보다는 작을(효율적일 수 있는) 최대 수
        if k ** 2 + (k - 1) ** 2 >= nums_of_home * m:
            break
        make_k_ij(k)
        for i in range(n):
            for j in range(n):
                count = 0
                for ii, jj in k_bucket[k]:
                    if i + ii >= 0 and i + ii <= n - 1 and j + jj >= 0 and j + jj <= n - 1 and mat[i + ii][j + jj]:
                        count += 1
                if count * m - (k ** 2 + (k - 1) ** 2) >= 0 and ans_count < count:
                    ans_count = count

    print('#%s %s' % (tc, ans_count))