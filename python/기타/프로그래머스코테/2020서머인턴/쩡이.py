def solution(n):
    answer = 0
    while True:
        q, r = calc_2(n)
        answer += 3 ** q
        if r <= 1:
            answer += r
            break
        n = r
    return answer


def calc_2(n):
    q = 0
    r = 0
    num = 1
    while True:
        num *= 2
        if num == n:
            q += 1
            r = 0
            break
        elif num > n:
            r = n - (num // 2)
            break
        q += 1
    return q, r


print(solution(10 ** 8))