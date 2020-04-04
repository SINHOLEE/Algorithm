def solution(n, lost, reserve):
    lis = [1] * n
    for lo in lost:
        lis[lo-1] -= 1
    for re in reserve:
        lis[re-1] += 1

    for i in range(n):
        if lis[i] == 2 and i-1 >= 0 and lis[i-1] == 0:
            lis[i] -= 1
            lis[i-1] += 1
        if lis[i] == 2 and i+1 < n and lis[i+1] == 0:
            lis[i] -= 1
            lis[i+1] += 1

    answer = 0
    for li in lis:
        if li > 0:
            answer += 1

    return answer


solution(7, [1, 3, 4, 6], [2, 5])
