t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    small = min(a,b)
    big = max(a,b)

    if small * 2 >= big:
        print((2*small) ** 2)
    else:
        print(big ** 2)