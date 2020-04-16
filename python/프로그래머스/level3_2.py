my_set = set()


def dfs(user_id, banned_id, cnt, len_banned, total_sum, visited):
    global my_set
    if cnt == len_banned:
        my_set.add(tuple(visited))
        return total_sum + 1

    for i in range(len(user_id)):
        if visited[i]:
            continue
        if len(user_id[i]) != len(banned_id[cnt]):
            continue
        for j in range(len(user_id[i])):
            if banned_id[cnt][j] == "*":
                continue
            if banned_id[cnt][j] != user_id[i][j]:
                break
        else:  # 전부 다 무사 통과
            visited[i] = 1
            total_sum = dfs(user_id, banned_id, cnt+1, len_banned, total_sum, visited)
            visited[i] = 0
    return total_sum


def solution(user_id, banned_id):
    global my_set
    len_banned = len(banned_id)
    visited = [0] * len(user_id)

    answer = dfs(user_id,banned_id, 0, len_banned, 0, visited)
    answer = len(my_set)
    return answer


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])