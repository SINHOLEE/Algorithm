T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    num_list = []
    for _ in range(M):
        num_list.append(list(map(int, input().split())))
# ​

    for i in range(1, M):
        check = True
        for j in range(len(num_list[0])):
            if num_list[0][j] > num_list[i][0]:
                num_list[0][j:0] = num_list[i]
                # print(num_list)
                check = False
                break
        if check:
            num_list[0].extend(num_list[i])

    print('#{} {}'.format(tc, ' '.join(map(str, num_list[0][-1:-11:-1]))))