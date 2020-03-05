
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    my_list = list(map(int, input().split()))
    my_len = len(my_list)
    my_sum = sum(my_list)
    dp = [1] + [0] * my_sum
    temp = [0]
    count = 1
    for i in my_list:
        for j in range(len(temp)):
            if dp[i + temp[j]] == 0:
                dp[i + temp[j]] = 1
                temp.append(i + temp[j])
                count += 1


    print('#%s %s' % (tc, count))


