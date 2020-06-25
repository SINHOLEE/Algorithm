def divide(s, e, big, small, total):
    global x
    if e<=s:
        return total
    n = (s+e) // 2
    if small >= n and big >= 2*n:
        t_small = small- n
        t_big = big - 2*n
        tt_big = max(t_big, t_small)
        tt_small = min(t_big, t_small)
        temp =

        return divide(n+1, e, big, small, n)
    else:
        return divide(s, n, big, small, total)

t = int(input())
for _ in range(t):
    x = 0
    a, b = map(int, input().split())
    big = max(a, b)
    small = min(a, b)
    divide(0, small, big, small)
    print(x)