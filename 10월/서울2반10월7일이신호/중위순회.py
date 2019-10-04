def tree(node):
    global s ,n

    if len(data[node][1]) == 0:
        s += data[node][0]
        return s
    elif len(data[node][1]) == 1:
        tree(int(data[node][1][0]))
        s += data[node][0]

        return s
    else:
        tree(int(data[node][1][0]))
        s += data[node][0]
        tree(int(data[node][1][1]))
        return s
for tc in range(1, 11):
    n = int(input())
    data = [[] for _ in range(n+1)]
    for _ in range(n):
        temp = list(map(str, input().split()))
        if len(temp) == 2:
            data[int(temp[0])] = (temp[1], [])
        else:
            data[int(temp[0])] = (temp[1], temp[2:])
    s = ''


    print('#%s %s' % (tc, tree(1)))