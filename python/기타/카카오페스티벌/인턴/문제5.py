stones = [1]
k = 1
def solution(stones, k):
    flag = False
    total_len = len(stones) # 11
    answer = 0
    current = -1
    while True:
        jump = 0
        for i in range(1, k+1): # 현재 위치에서 i만큼 점프할 수 있다.
            if current + i < total_len and stones[current + i] != 0:
                jump = i
                flag = False
                break
            else:
                if current + i > total_len -1:
                    flag = True
                    break
                continue
        if flag:
            current = -1
            answer += 1
            continue

        if jump == 0:
            break
        if current + jump >= total_len - 1:
            if current + jump == total_len - 1:
                stones[current+jump] -= 1
            current = -1
            answer += 1
            continue

        stones[current + jump] -= 1
        current = current+jump
    return answer

print(solution(stones, k))
