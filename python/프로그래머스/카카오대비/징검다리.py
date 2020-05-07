# 이분탐색...흠...

def check(target, stones, k):
    global s_len
    temp = 0
    for i in range(s_len):
        if stones[i] < target:
            temp += 1
        else:
            temp = 0
        if temp >= k:
            return False
    return True


def solution(stones, k):
    global s_len
    answer = 0  # 넘어갈 수 있는 사람의 수
    s_len = len(stones)
    s = min(stones)
    e = max(stones)
    m = (s+e) // 2  # idx and value
    while True:
        if e < s:
            break
        if check(m, stones, k):
            answer = m
            s = m + 1
            m = (s + e) // 2
        else:
            e = m - 1
            m = (s+e) // 2

    # 이분탐색으로 target으로 모두 건널 수 있으면, answer를 target으로 갱신하고, right이분탐색 진행, 아니면 left 이분탐색 진행
    return answer


s_len = 0
solution([8, 8, 9, 10, 10, 10, 10, 10, 10, 10], 3)