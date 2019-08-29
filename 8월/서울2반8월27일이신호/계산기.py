inner = ['(', '+', '*']
outter = ['', '+', '*', '(']

for tc in range(1, 11):
    N = int(input())
    string = input()
    s1 = ''
    mystack = [''] * 100000
    top = -1
    i = 0
    while True:
        if len(string) == i:
            break
        if string[i] == '+' or string[i] == '*' or string[i] == '(' or string[i] == ')':
            if top == -1:
                top += 1
                mystack[top] = string[i]
            else:
                if string[i] == ')':
                    while True:
                        if mystack[top] == '(':
                            top -= 1
                            break
                        s1 += mystack[top]
                        top -= 1
                else:
                    if outter.index(string[i]) > inner.index(mystack[top]):
                        top += 1
                        mystack[top] = string[i]
                    else:
                        while True:
                            if inner.index(mystack[top]) < outter.index(string[i]):
                                top += 1
                                mystack[top] = string[i]
                                break
                            if top == -1:
                                top += 1
                                mystack[top] = string[i]
                                break
                            s1 += mystack[top]
                            top -= 1

        else:
            s1 += string[i]
        i += 1
    i = 0
    calstack = ['']*100000
    while True:
        if len(s1) == i:
            result = calstack[0]
            break

        if s1[i] == '+':
            back = calstack[top]
            top -= 1

            front = calstack[top]
            top -= 1

            cnt = int(front) + int(back)

            top += 1
            calstack[top] = cnt

        elif s1[i] == '*':
            back = calstack[top]
            top -= 1

            front = calstack[top]
            top -= 1

            cnt = int(front) * int(back)

            top += 1
            calstack[top] = cnt
        else:
            top += 1
            calstack[top] = s1[i]

        i += 1



    print('#{} {}'.format(tc, result))

