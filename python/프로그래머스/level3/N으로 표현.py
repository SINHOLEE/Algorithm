def dfs(N, cnt, res, number):
    global global_min, t
    t += 1
    if cnt > 8:
        return
    if res == number:
        if cnt < global_min or global_min == -1:
            global_min = cnt
        return
    temp = 0
    for i in range(8):
        temp = 10 * temp + N
        dfs(N, cnt+i+1, res + temp, number)
        dfs(N, cnt+i+1, res - temp, number)
        dfs(N, cnt+i+1, res * temp, number)
        dfs(N, cnt+i+1, res // temp, number)


def solution(N, number):
    global global_min
    dfs(N,0, 0, number)
    return global_min
t = 0
global_min = -1
print(solution(9, 70))

