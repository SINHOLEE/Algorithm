n, capital = map(int, input().strip().split())
adj_list = [[] for i in range(n+1)]
water = [0] * (n+1)
water[capital] = 1
for i in range(n):
    a, b = map(int, input().split())
    adj_list[b].append(a)


