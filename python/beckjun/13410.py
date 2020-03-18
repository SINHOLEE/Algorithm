def reverse(num):
    temp = 0
    while True:
        if num == 0:
            break
        temp *= 10
        temp += num % 10
        num = num // 10
    return temp


n, m = map(int, input().split())

res = 0
for i in range(1, m+1):
    res = max(res, reverse(n * i))
print(res)
