def solution(weight):
    weight.sort()
    if weight[0] >= 2:
        return 1
    else:
        target = 1
        for i in range(len(weight)-1):
            target += weight[i]
            if target < weight[i+1]:
                return target

        return target + weight[-1]


print(solution([1, 3]))
