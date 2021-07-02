def reverse(u):
    temp = ""
    for i in u[1:-1]:
        if i == "(":
            temp += ")"
        else:
            temp += "("
    return temp


def iscorrect(p):
    cnt = 0
    for chracter in p:
        if chracter == '(':
            cnt += 1
        else:
            if cnt > 0:
                cnt -= 1
            else:
                return False
    return True


def solution(p):
    if len(p) == 0:
        return ""
    cnt = 0
    for i in range(len(p)+1):
        if i != 0 and cnt == 0:
            u = p[:i] # 균형잡힌 괄호 문자열
            v = p[i:]
            break
        if p[i] == "(":
            cnt += 1
        else:
            cnt -= 1
    if iscorrect(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + reverse(u)


print(solution(")())((()"))
