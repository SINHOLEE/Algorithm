def divied_search(s, e, d):
    global lis
    if e-s == 1:
        return
    mid = (s+e) // 2
    if d == 0:  # 왼쪽
        lis[mid] = 0
    else:
        lis[mid] = 1
    divied_search(s,mid,0)
    divied_search(mid,e,1)


def solution(n):
    global lis
    new_len = 2 ** n + 1
    lis = [-1] * new_len
    divied_search(0, new_len-1, 0)
    return lis[1:-1]


lis = []


solution(20)