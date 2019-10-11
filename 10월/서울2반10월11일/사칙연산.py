def tree(node):
    if lis[node][1] not in ('-', '+', '*', '/'):
        return float(lis[node][1])
    else:
        if lis[node][1] == '+':
            return float(tree(int(lis[node][2]))) + float(tree(int(lis[node][3])))
        elif lis[node][1] == '-':
            return float(tree(int(lis[node][2]))) - float(tree(int(lis[node][3])))
        elif lis[node][1] == '*':
            return float(tree(int(lis[node][2]))) * float(tree(int(lis[node][3])))
        else:
            return float(tree(int(lis[node][2]))) / float(tree(int(lis[node][3])))


for tc in range(1, 11):
    N = int(input())
    lis = [[]]
    for _ in range(N):

        temp = list(map(str, input().split()))
        lis.append(temp)
    print('#%s %s' % (tc,int(tree(1))))