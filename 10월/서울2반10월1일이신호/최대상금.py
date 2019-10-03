# 초 비효율 코드
T = int(input())

def perm(depth, lis):
    global my_max1, my_num, count
    count += 1
    if depth == n_len:
        string = ''.join(lis)
        num = int(string)

        for i in range(n_len):
            combi(0, i, lis, num)

        return

    for j in range(n_len):
        if visited[j] == False:
            visited[j] = True
            perm(depth+1, lis+[n[j]])
            visited[j] = False


def combi(depth, i, lis, num1):
    global my_max, my_num, count
    count += 1
    if depth == 1:
        string = ''.join(lis)
        num = int(string)
        my_num = num
        if num1 not in dic:
            dic[num1] = [my_num]
        else:
            if my_num not in dic[num1]:
                dic[num1].append(my_num)
        if my_max < num:
            my_max = num
        return

    for j in range(i+1, n_len):

            lis[i], lis[j] = lis[j], lis[i]
            combi(depth+1, j, lis, num1)
            lis[i], lis[j] = lis[j], lis[i]

def find(key, cnt):
    if cnt == k:
        return max(dic[key])

    if key in dp[cnt]:
        return dp[cnt][key]

    result = 0
    for i in dic[key]:
        a = find(i, cnt+1)
        if result < a:
            result = a
    dp[cnt][key] = result

    return result





for tc in range(1, T+1):
    n, k = map(str, input().split())
    n = list(n)
    n_len = len(n)
    k = int(k)
    dic = {}
    temp = []
    my_max = 0
    visited = [False] * n_len
    count = 0
    perm(0, temp)
    string = ''.join(n)
    num = int(string)
    result = 0
    dp = [{} for _ in range(k+1)]
    find(num, 0)
    print(dic)
    print(count)
    # print('#%s %s' %  (tc, result))



