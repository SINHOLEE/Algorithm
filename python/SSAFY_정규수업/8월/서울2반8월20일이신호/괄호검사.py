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


# T = int(input())
#
# for tc in range(1, T+1):
#     s = input()
#     top = -1
#     mystack = [''] * len(s)
#
#     result = 1
#     for chr_id in range(len(s)):
#         #  짝이 맞는지만 검사
#         if s[chr_id] == '(' or s[chr_id] == '{':
#             top += 1
#             mystack[top] = s[chr_id]
#         elif s[chr_id] == ')':
#
#             if top == -1:
#                 result = 0
#                 break
#             else:
#                 if mystack[top] == '(':
#                     top -= 1
#                 else:
#                     result = 0
#                     break
#
#         elif s[chr_id] == '}':
#             if top == -1:
#                 result = 0
#                 break
#             else:
#                 if mystack[top] == '{':
#                     top -= 1
#                 else:
#                     result = 0
#                     break
#         else:
#             pass
#
#     if top == -1 and result == True:
#         result = 1
#     else:
#         result = 0
#
#     print('#{} {}'.format(tc, result))


# 교수님 풀이
T = int(input())

for tc in range(1, T+1):
    data = input()
    mystack = []
    for i in range(len(data)):
        if data[i] == '(' or data[i] == '{':
            mystack.append(data[i])
        elif data[i] == ')' or data[i] == '}':
            if len(mystack) == 0:
                mystack.append(data[i]) # 여는 놈이 나오기 전에 닫는놈이 나오면 mystack에 담고 브레이크
                break
            elif ( data[i] == ')' and mystack[-1] != '(' ) or ( data[i] == '}' and mystack[-1] != '{' ):
                mystack.append(data[i])  # mystack에 마지막 애랑 지금 닫으려는 애랑 매칭이 안되면 오류 그치만 어팬드 안해도 될거같은데?
                break
            else:
                mystack.pop()



if len(mystack):
    print('1')
else:
    print('0')