def sub_solve():
    n, x = map(int, input().split())
    lis = [*map(int, input().split())]
    max_len = 0
    for i in range(n):
        sum = lis[i]
        if sum % x != 0:
            max_len = max(max_len, 1)
        if n-i+1 < max_len:
            break
        for j in range(i+1, n):
            sum+= lis[j]
            if sum % x != 0:
                max_len = max(max_len, j-i+1)
    if max_len:
        return max_len
    else:
        return -1


for _ in range(int(input())):
    print(sub_solve())

