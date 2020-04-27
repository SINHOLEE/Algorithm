def solution(S):
    S = S.split(" ")
    stack = []
    for s in S:
        if s == "DUP":
            if len(stack) > 0:
                stack.append(stack[-1])
            else:
                return -1
        elif s == "POP":
            if len(stack) > 0:
                stack.pop()
            else:
                return -1
        elif s == "+":
            if len(stack) > 1:
                temp = stack.pop()
                stack[-1] += temp
            else:
                return -1
        elif s == "-":
            if len(stack) > 1:
                temp1 = stack.pop()
                temp2 = stack.pop()
                stack.append(temp1-temp2)
                if stack[-1] < 0:
                    return -1
            else:
                return -1
            pass
        else:
            stack.append(int(s))
    if len(stack) > 0:
        return stack[-1]
    else:
        return -1


print(solution('13 DUP 4 POP 5 DUP + DUP + - POP'))
