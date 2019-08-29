T = int(input())

for tc in range(1, T+1):
    string = input()
    string += '#'
    count = 0
    while count != len(string)-1 and len(string) != 0:
        count = 0
        for chr in range(0, len(string) - 1):
            if string[chr] == string[chr+1]:
                string = string[:chr]+string[chr+2:]
                break
            else:
                count += 1

    print('#{} {}'.format(tc, len(string) - 1))


T = int(input())

for tc in range(1, T+1):
    string = input()

    mystack = [''] * 1001
    top = -1
    for i in range(len(string)):
        if mystack:
            if mystack[top] == string[i]:
                top -= 1
            else:
                top += 1
                mystack[top] = string[i]
        else:
            mystack.append(string[i])
    print('#{} {}'.format(tc, top + 1))