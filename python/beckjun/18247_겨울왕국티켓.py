for i in range(int(input())):
    r, c = map(int, input().split())
    if r < 12:
        print(-1)
    elif c < 4:
        print(-1)
    else:
        print(11 * c + 4)
