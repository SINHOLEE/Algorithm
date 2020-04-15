def solution(inputString):
    a = 0  # <>
    b = 0  # ()
    c = 0  # []
    d = 0  # {}
    res = 0
    flag = False
    for i in inputString:
        if i == '>':
            if a >= 1:
                res += 1
                a -= 1
            else:
                flag = True
                break
        if i == ')':
            if b >= 1:
                res += 1
                b -= 1
            else:
                flag = True
                break

        if i == ']':
            if c >= 1:
                res += 1
                c -= 1
            else:
                flag = True
                break

        if i == '}':
            if d >= 1:
                res += 1
                d -= 1
            else:
                flag = True
                break

        if i == '<' :
            a += 1
        if i == '(':
            b += 1
        if i == '[':
            c += 1
        if i == '{':
            d += 1

    if flag:
        return -1
    return res


print(solution('if (Count of eggs is 4.) {Buy milk.}'))
