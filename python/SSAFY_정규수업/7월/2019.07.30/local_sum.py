T = int(input())

for t in range(1, T + 1):
    N, M = input().split()
    N = int(N)
    M = int(M)
    nums = list(map(int, input().split()))

    # sorting_ nums

    min_sum = 0
    max_sum = 0
    for i in range(len(nums) - M + 1):
        min_temp = 0
        max_temp = 0
        for j in range(M):
            if i == 0:
                min_sum += nums[i + j]
                max_sum += nums[i + j]
            else:

                min_temp += nums[i + j]
                if j == M - 1:
                    if min_sum > min_temp:
                        min_sum = min_temp
                else:
                    pass
                max_temp += nums[i + j]
                if j == M - 1:
                    if max_sum < max_temp:
                        max_sum = max_temp
                else:
                    pass

    print('#{} {}'.format(t, max_sum - min_sum))




