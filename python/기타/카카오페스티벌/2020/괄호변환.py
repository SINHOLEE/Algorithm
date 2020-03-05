p = ")()()()("
def is_right(u):

    stack = []
    e = 0
    for c in u:
        if c =='(':
            e+=1
        else:
            e-=1
        if e <0:
            return False
    return True

def fn(w):
    if len(w) == 0:
        return w
    cnt = 0
    for i in range(len(w)):
        if w[i] == '(':
           cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            last_idx = i + 1
            break

    u = w[:last_idx]
    v = w[last_idx:]
    v = fn(v)
    if is_right(u):
        return u + v
    else:
        new_string = "(" + v + ")"
        for i in range(1, len(u)-1):
            if u[i] == '(':
                new_string += ')'
            else:
                new_string += '('
        return new_string
def solution(p):

    answer = fn(p)
    return answer
print(solution(p))
