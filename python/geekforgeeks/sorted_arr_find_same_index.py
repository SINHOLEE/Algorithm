def solution(lis):
    s = 0
    e = len(lis) - 1

    if s == lis[0]:
        return s
    if e == lis[e]:
        return e

    res = -1
    while s <= e:
        m = (s + e) // 2
        if lis[m] == m:
            res = m
            break
        if lis[m] < m:
            s = m + 1
        else:
            e = m - 1
    return res


print(solution([-10, -5, 0, 3, 7]))
print(solution([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]))
print(solution([-10, -5, 3, 4, 7, 9]))
