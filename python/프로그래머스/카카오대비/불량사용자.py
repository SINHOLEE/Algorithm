def solution(user_id, banned_id):
    global answer
    answer = 0
    bucket = set()
    len_user_id = len(user_id)
    len_banned_id = len(banned_id)
    visited = [0] * len_user_id

    def check(lis):
        for i in range(len_banned_id):
            if len(lis[i]) != len(banned_id[i]):
                return False
            for j in range(len(lis[i])):
                if banned_id[i][j] == '*':
                    continue
                if banned_id[i][j] != lis[i][j]:
                    return False
        return True

    def perm(depth, lis):
        global answer
        if depth == len_banned_id:
            if check(lis):
                bucket.add(tuple(sorted(lis)))
        for i in range(len_user_id):
            if visited[i]:
                continue
            visited[i] = 1
            perm(depth + 1, lis + [user_id[i]])
            visited[i] = 0

    perm(0, [])
    return len(bucket)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
