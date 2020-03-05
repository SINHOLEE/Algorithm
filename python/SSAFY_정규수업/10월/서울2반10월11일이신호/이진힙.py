T = int(input())

def solution(idx):
    if idx == 1:
        return my_tree[1]
    else:
        return solution(min_heap_CtoP[idx]) + my_tree[idx]

for tc in range(1, T+1):
    n = int(input())
    min_heap_PtoC = [[] for _ in range(n+1) ]
    temp = list(map(int, input().split()))

    min_heap_CtoP =  [-1] * (n+1)
    cnt = 1
    flag = 0
    for i in range(2, n+1):
        min_heap_CtoP[i] = cnt

        if flag == 0:
            flag += 1
            continue
        else:
            cnt += 1
            flag = 0


    my_tree = [-1] * (n+1)

    p = -1
    c = -1
    for i in range(n):
        if my_tree[i+1] == -1:
            my_tree[i+1] = temp[i]
        if i >= 1:
            ii = i+1
            while True:
                if my_tree[min_heap_CtoP[ii]] < my_tree[ii]:
                    break
                my_tree[min_heap_CtoP[ii]], my_tree[ii] = my_tree[ii], my_tree[min_heap_CtoP[ii]]
                ii = min_heap_CtoP[ii]

    print('#%s %s' % (tc, solution(min_heap_CtoP[n])))


