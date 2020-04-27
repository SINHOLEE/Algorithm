def solution(N, stages):
    len_stages = len(stages)
    arr = [0] * (N+1)
    for stage in stages:
        if int(stage) == N+1:
            continue
        arr[int(stage)] += 1

    answer = []
    for i in range(1, N+1):
        if len_stages == 0:
            answer.append((0, i))
        else:
            answer.append((arr[i] / len_stages, i))
            len_stages -= arr[i]

    answer.sort(key=lambda x:x[0], reverse=True)
    answer = list(map(lambda x: x[1], answer))
    return answer


solution(	4, [5,5,4,5,5,5])
