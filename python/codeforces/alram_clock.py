t = int(input())

for i in range(t):
    a, b, c, d = tuple(map(int, input().split()))

    if a <= b:
        print(b)
        continue
    last_time = a-b

    if c <= d:
        print(-1)
        continue

    if last_time % (c-d) == 0:
        print(b + (last_time//(c-d)) * c)
    else:
        print(b + (last_time // (c - d) + 1) * c)
1