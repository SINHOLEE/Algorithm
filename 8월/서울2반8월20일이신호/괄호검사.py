# T = int(input())
#
# for tc in range(1, T+1):
#     words = input()
#     my_stack = []
#     my_dict = {
#         '{' : '}',
#         '(' : ')',
#     }
#     switch = 0
#     for chr in words:
#         if len(my_stack) == 0:
#             if chr == '{' or chr == '(':
#                 my_stack += [chr]
#             elif chr == '}' or chr == ')':
#                 switch = 1
#                 break
#         else:
#             if chr == '{' or chr == '(':
#                 my_stack += [chr]
#             if chr == my_dict[my_stack[-1]]:
#                 my_stack.pop(-1)
#
#     if switch == 1:
#         result = 0
#     else:
#         if len(my_stack) == 0:
#             result = 1
#         else:
#             result = 0
#
#     print('#{} {}'.format(tc, result))


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



