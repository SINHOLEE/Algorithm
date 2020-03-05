T = int(input())

for tc in range(1, T+1):
    s = input()
    top = -1
    mystack = [''] * len(s)


    result = 1
    for chr_id in range(len(s)):
        if s[chr_id] == '(' or s[chr_id] == '{':
            top += 1
            mystack[top] = s[chr_id]
        elif s[chr_id] == ')':
            if top == -1:
                result = 0
                break
            else:
                if mystack[top] == '(':
                    mystack[top] == 0
                    top -= 1
                else:
                    result = 0
                    break

        elif s[chr_id] == '}':
            if top == -1:
                result = 0
                break
            else:
                if mystack[top] == '{':
                    mystack[top] == 0
                    top -= 1
                else:
                    result = 0
                    break
        else:
            pass

    if top == -1 and result == True:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(tc, result))