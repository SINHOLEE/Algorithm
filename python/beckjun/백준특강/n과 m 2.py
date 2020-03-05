n,m = map(int, input().split())

def sub_set_combi(depth, n,m, lis):
    if depth == n:
        print(visited)
        return

    sub_set_combi(depth+1, n, m, )
    sub_set_combi(depth+1, n, m)


visited = [0] * n
