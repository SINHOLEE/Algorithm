def solution(stones,k):
    answer = float('inf')
    tmp = []
    for idx, stone in enumerate(stones):
        tmp.append(stone)
        print(idx, stone)
        print(tmp)
        print()
        if idx < k-1:
            continue
        value = max(tmp)
        answer = (value < answer) and value or answer
        tmp.pop(0)

    return answer


solution([8, 8, 9, 10, 10, 10, 10, 10, 10, 10], 3)
