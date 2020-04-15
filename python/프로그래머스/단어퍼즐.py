from collections import deque


def solution(strs, t):
    t_n = len(t)
    len_str = len(strs)
    n_strs = [0] * len_str
    for idx in range(len_str):
        n_strs[idx] = len(strs[idx])

    adj_list = [[] for _ in range(t_n)]
    for i in range(t_n):
        for id in range(len_str):
            if t[i:i+n_strs[id]] == strs[id]:
                adj_list[i].append(i+n_strs[id])
    q = deque([(0, 0)])
    visited = [0] * (t_n+1)
    answer = -1
    while q:
        idx, cnt = q.popleft()
        if idx == t_n:
            return cnt
        for nxt in adj_list[idx]:
            if visited[nxt]:
                continue
            visited[nxt] = 1
            q.append((nxt, cnt+1))

    # # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    return answer


print(solution(["ba", "an", "nan", "ban", "n"], 'banana'))
