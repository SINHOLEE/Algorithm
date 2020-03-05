T = int(input())

for tc in range(1, T+1):
    words = list(input())
    target = list(input())
    length = len(words)
    len_target = len(target)
    cnt = 0
    j = 0
    temp = words[0:len_target]
    for i in range(length-len_target+1):

        if temp == target:
            cnt += 1
        temp = words[len_target+i+1]

    print('#%s %s' % (tc, cnt))
