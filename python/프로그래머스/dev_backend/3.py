def dfs(numbers, K, cnt):
    global cache, res
    t_numbers = tuple(numbers)
    if cache.get(t_numbers) is None:
        cache[t_numbers] = cnt
    else:
        if cache[t_numbers] > cnt:
            cache[t_numbers] = cnt
    if cache[t_numbers] < cnt:
        return

    if res < cnt:
        return
    # 조건에 부합하는지 판단.
    for i in range(1, len(numbers)):
        if abs(numbers[i] - numbers[i-1]) > K:
            break
    else:
        res = min(res, cnt)
        return

        # swap1 원소  찾기
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if i == j:
                continue
            numbers[i], numbers[j] = numbers[j], numbers[i]
            dfs(numbers,K, cnt+1)
            numbers[i], numbers[j] = numbers[j], numbers[i]


def solution(numbers, K):
    global res, cache

    dfs(numbers, K, 0)
    print(res)
    return -1 if res == 4 else res


cache = {}
res = 9
solution([3, 7, 2, 8, 6, 4, 5, 1], 1)


