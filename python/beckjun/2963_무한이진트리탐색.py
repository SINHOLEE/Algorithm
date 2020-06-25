def solve():
    op = input()
    cnt = 0
    x = 1
    for target in op:
        if target == "*":
            cnt += 1
            x = 5 * x + 3 ** (cnt-1)
        else:
            if target == "L":
                x = 2*x
            elif target == "R":
                x = 2 * x + 3 ** cnt

    return x


print(solve())
