from pprint import pprint

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    visited = [False] * (n+1)
    mat = [[] for i in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        mat[a].append(b)
        mat[b].append(a)
    my_set = set()
    my_set.update(mat[1])
    for i in mat[1]:
        my_set.update(mat[i])
    my_set -= {1}
    cnt = 0
    for i in my_set:
        cnt += 1
    print('#%s %s' % (tc, cnt))