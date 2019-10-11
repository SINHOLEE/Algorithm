# 첫번째 방식
T = int(input())
def tree(v):
    if not node[v]:
        return 1
    else:
        if len(node[v]) == 2:
            a = tree(node[v][0])
            b = tree(node[v][1])
            return a + b + 1
        else:
            return tree(node[v][0]) + 1

for tc in range(1, T+1):
    e, n = map(int, input().split())
    node = [[] for _ in range(e+2)]
    temp = list(map(int, input().split()))
    for i in range(0, e*2, 2):
        node[temp[i]].append(temp[i+1])

    print('#%s %s' % (tc, tree(n)))

# 두번째 방식
T = int(input())
def tree(v):
    if not node[v]:
        return 1
    else:
        sub_sum = 1
        for i in node[v]:
            sub_sum += tree(i)
        return sub_sum
for tc in range(1, T+1):
    e, n = map(int, input().split())
    node = [[] for _ in range(e+2)]
    temp = list(map(int, input().split()))
    for i in range(0, e*2, 2):
        node[temp[i]].append(temp[i+1])

    print('#%s %s' % (tc, tree(n)))