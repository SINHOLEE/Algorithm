def find(idx, money):
    global min_fee, c
    c+=1
    if idx >= 12:
        if min_fee > money:
            min_fee = money
        return

    if dp[idx] > money:
        dp[idx] = money
    else:
        return

    if money > min_fee:
        return

    if plan[idx] == 0:
        find(idx+1, money)
    else:
        find(idx+1, money + prices[0] * plan[idx])
        find(idx+1, money + prices[1])
        find(idx+3, money + prices[2])
        find(idx+12, money + prices[3])


T = int(input())
for tc in range(1, T+1):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    min_fee = 9999999
    c = 0
    dp = [9999999999999] * 12
    find(0, 0)
    print('#%s %s' % (tc, min_fee))
    print(c)