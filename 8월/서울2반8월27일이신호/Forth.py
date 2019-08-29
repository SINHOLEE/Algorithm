T = int(input())
for tc in range(1, T+1):
    my_code = list(map(str, input().split()))

    i = 0
    top = -1
    mystack = [''] * 100

    try:
        while True:
            if my_code[i] == '.':
                break

            if my_code[i] == '+' or my_code[i] == '-' or my_code[i] == '/' or my_code[i] == '*':
                if my_code[i] == '+':
                    back = mystack[top]
                    top -= 1
                    front = mystack[top]
                    top -= 1

                    new_num = int(front) + int(back)
                    top += 1
                    mystack[top] = new_num

                if my_code[i] == '-':
                    back = mystack[top]
                    top -= 1
                    front = mystack[top]
                    top -= 1

                    new_num = int(front) - int(back)
                    top += 1
                    mystack[top] = new_num

                if my_code[i] == '*':
                    back = mystack[top]
                    top -= 1
                    front = mystack[top]
                    top -= 1

                    new_num = int(front) * int(back)
                    top += 1
                    mystack[top] = new_num

                if my_code[i] == '/':
                    back = mystack[top]
                    top -= 1
                    front = mystack[top]
                    top -= 1

                    new_num = int(front) / int(back)
                    top += 1
                    mystack[top] = int(new_num)

            else:
                top += 1
                mystack[top] = my_code[i]

            i += 1

        result = mystack[0]
        if top != 0 or (len(my_code) - 1) != my_code.index('.'):
            print('#{} error'.format(tc))
            pass
        else:

            print('#{} {}'.format(tc, result))

    except:
        print('#{} error'.format(tc))

