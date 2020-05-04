def solution(path):
    path_list = path.split('/')
    stack = []
    for dir in path_list:
        if dir == '..':
            if len(stack) and stack[-1] != '..':
                stack.pop()
            else:
                stack.append(dir)
        elif dir == '.':
            pass
        else:
            stack.append(dir)

    return '/'.join(stack)


print(solution('/home/user/temp/../temp/../test.txt'))
print(solution('../../.././.././adfs.txt'))
print(solution('.././asdf/'))
