def solution(n):
    answer = 0
    total = 1
    e = 1
    while True:
        if n == 1:
            target = 1
            e = 0
            break
        if total +1 + total >= n:
            target = total+1
            break
        e += 1
        total = total+1+total
    n = n-target

    if n == 0:
        return 3 ** e
    lis = [1, 3, 4]
    cnt = 2
    exp = 2
    while True:
        if cnt+1 >= n:
            break
        new_lis = [3 ** exp]
        cnt += 1
        if cnt+1 == n:
            lis+=new_lis
            break
        for item in lis:
            new_lis.append(new_lis[0] + item)
            cnt+=1
            if cnt + 1 == n:
                lis+=new_lis
                break
        else:
            lis += new_lis
        exp+=1
    return 3 ** e + lis[n-1]


# print(solution(10 ** 8))

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


print(solution(10 ** 10))