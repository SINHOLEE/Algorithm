'''
탐색종료시점을 잘 생각하자.
if min_score ==0:
    break
이거 하나로 몇배나 빨라졌다.
'''
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
def cal(lis1):
    lis2 = list(filter(lambda x: x not in lis1, range(n)))
    l = len(lis1)
    a_val = 0
    b_val = 0
    visited = [0] * l
    for i in range(l):
        visited[i] = 1
        for j in range(i+1, l):
            if j > i and visited[j] == 0:
                a_val = a_val + mat[lis1[i]][lis1[j]] + mat[lis1[j]][lis1[i]]
                b_val = b_val + mat[lis2[i]][lis2[j]] + mat[lis2[j]][lis2[i]]
        visited[i] = 0

    return abs(a_val - b_val)


def comp(a, depth, now):
    global min_score, check
    if check:
        return
    if depth == n//2:
        sub_val = cal(a)
        if min_score > sub_val:
            min_score = sub_val
        if min_score == 0:
            check = True
        return

    for i in range(now+1,n):
        if visited[i] == 0:
            visited[i] = 1
            comp(a+[i], depth+1, i)
            visited[i] = 0
min_score = 99998989898989
visited = [0] * n
check = False
for i in range(n):
    visited[i] = 1
    if check:
        break
    comp([i],1,i)
    visited[i] = 0
print(min_score)
