def num_of_perm(N):
    if N == 1:
        return 1
    else:
        return N * num_of_perm(N-1)

def solution(depth, total, right, rest_weight, idx):
    global count, length,c
    c += 1
    if depth == length:
        count += 1
        return

    if total > right + rest_weight:
        count += num_of_perm(length - depth) * 2 **(length - depth)
        return


    for i in range(length):


        if visited[i] == False:
            visited[i] = True
            solution(depth + 1, total + cheues[i], right, rest_weight - cheues[i], i) #왼
            if right + cheues[i] <= total:# 오
                solution(depth+1, total, right + cheues[i], rest_weight - cheues[i], i )
            visited[i] = False
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cheues = sorted(list(map(int, input().split())))
    sum_of_cheues = sum(cheues)
    length = len(cheues)
    count = 0
    c = 0
    visited = [False] * length
    solution(0, 0, 0, sum_of_cheues, -1)
    print('#%s %s' % (tc,count))
