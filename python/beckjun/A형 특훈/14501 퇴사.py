# n = int(input())
#
# cost = [0] * n
# revenue = [0] * n
# for _ in range(n):
#     a, b = map(int, input().split())
#     cost[_] = a
#     revenue[_] = b
#
# def fn(day, res):
#     global max_revenue
#     if day + cost[day] > n-1:
#         if day+cost[day] == n:
#             res += revenue[day]
#         if max_revenue <res:
#             max_revenue = res
#         return
#     for k in range(day+cost[day], n):
#         fn(k, res+revenue[day])
#
# max_revenue = 0
# for i in range(n):
#     fn(i, 0)
#
# print(max_revenue)


N = int(input())
time = list(list(map(int, input().split())) for _ in range(N))
dp = [0] * N


for i in range(N):
    if i + time[i][0] <= N:
        dp[i] = time[i][1]
        for j in range(i):
            if j + time[j][0] <= i:
                dp[i] = max(dp[i], dp[j] + time[i][1])

print(max(dp))