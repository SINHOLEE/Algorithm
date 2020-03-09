has = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]


def transfer(num, n):
    res = ""
    while num != 0:
        res += has[num%n]
        num = num // n
    return res[::-1]


def solution(n, t, m, p):
    if p == 1:
        answer = "0"
        cnt = 1
    else:
        answer = ''
        cnt = 1
    num = 0
    while len(answer) != t:
        temp = transfer(num, n)
        for c in temp:
            if (cnt % m) == p-1:
                answer += c
            cnt += 1
            if len(answer) == t:
                return answer

        num += 1
    return answer


n,t,m,p = 16, 16, 2, 2
print(solution(n,t,m,p))
