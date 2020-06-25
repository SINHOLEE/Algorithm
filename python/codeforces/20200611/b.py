def solve1(a, b):
    a1 = a // 2
    b1 = b // 2

    if a == 0 or b == 0:
        return 0
    if a == 1 or b == 1:
        return 1
    if a == b:
        return a // 2

    res = -1

    if a < b:
        res = min(b1, a)
    else:
        res = min(a1, a)

    if abs(a - b) <= 3:
        res += 1

    return res


def solve():
    n, x, m = map(int, input().split())
    end = x
    start = x
    for i in range(m):
        l, r = map(int, input().split())
        if r < start:
            continue
        if end < l:
            continue
        start = min(start, l)
        end = max(end, r)

    return end - start + 1


t = int(input())
for _ in range(t):
    print(solve())
