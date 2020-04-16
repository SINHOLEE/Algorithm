n = int(input())
dic = [n+1] * (n+1)
dic[n] = 0


def dfs(cnt=0, cur_num=n):
    if cur_num == 1:
        dic[cur_num] = min(dic[cur_num], cnt)
        return dic[cur_num]
    if dic[1] < cnt:
        return dic[cur_num]
    if dic[cur_num] < cnt:
        return dic[cur_num]

    for k in [3, 2, 1]:
        if k == 2 or k == 3:
            if cur_num % k:
                continue
            dic[cur_num] = min(dfs(cnt+1, cur_num // k), cnt)
        else:
            dic[cur_num] = min(dfs(cnt+1, cur_num-1), cnt)
    return dic[cur_num]


dfs()
print(dic[1])
