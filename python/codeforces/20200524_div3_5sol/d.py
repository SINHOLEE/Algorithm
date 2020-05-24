
t = int(input())
for i in range(t):
    n, k = map(int, input().split())

    lis = []
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            lis.append(i)
            lis.append(n // i)
    lis.sort(reverse=True)

    for num in lis:
        if num <=k:
            print(n // num)
            break