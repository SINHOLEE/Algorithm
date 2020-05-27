t = int(input())

for i in range(t):
    n, m = map(int,input().split())
    target = n * m
    if target % 2:
        print(target // 2 + 1)
    else:
        print(target // 2)
