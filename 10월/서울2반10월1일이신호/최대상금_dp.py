#-*- coding: utf-8 -*-

T = int(input())

def combi(depth, length, tem, i):
    if depth == 2:
        able_ij.append(tem)
        return
    for j in range(i+1, length):
        if visited[j] == False:
            visited[j] = True
            combi(depth+1, length, tem + [j], j)
            visited[j] = False
def swap(a, b, lis):
    lis[a], lis[b] = lis[b], lis[a]
    return lis

def solution(k, lis):
    global a_len
    string = ''.join(lis)
    num = int(string)

    if k == 0:
        return num

    if num in dp[k]:
        return dp[k][num]

    my_max = 0
    for a, b in able_ij:
        swap(a, b, lis)
        temp = solution(k - 1 ,lis )
        swap(a, b, lis)
        if my_max < temp:
            my_max = temp
    dp[k][num] = my_max
    return dp[k][num]




for tc in range(1, T+1):
    n, k = map(str, input().split())
    n = list(n)
    n_len = len(n)
    k = int(k)

    able_ij = []  # [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
    a_len = len(able_ij)
    temp = []
    visited = [False] * n_len
    for i in range(n_len):
        visited[i] = True
        combi(1, n_len, temp + [i], i)
        visited[i] = False

    dp = [{} for _ in range(k+1)]

    solution(k, n)
    string = ''.join(n)
    num = int(string)
    # print(dp)
    print('#%s %s' % (tc, dp[k][num]))


