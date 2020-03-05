user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]


def solution(user_id, banned_id):
    visited = [False] * len(user_id)



    def isSame(user, baned):
        flag = False
        if len(user) == len(baned):
            for i in range(len(user)):
                if baned[i] == '*':
                    continue
                if baned[i] != user[i]:
                    flag = True
                    break
            if flag:
                return False
            else:
                return True

        else:
            return False


    bucket = [[] for i in range(len(banned_id))]
    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            if isSame(user_id[j], banned_id[i]):
                bucket[i].append(j) # user_id의 인덱스값 , user_id의 값
    my_set = []
    answer = 0
    def comp(row, item, depth, lis):
        global answer
        if depth == len(banned_id)-1:
            lis = set(lis)
            if lis not in my_set:
                my_set.append(lis)
            return
        for i in range(row+1, len(bucket)):
            for j in range(len(bucket[i])):
                if visited[bucket[i][j]] == False:
                    visited[bucket[i][j]] = True
                    comp(i, bucket[i][j], depth+1, lis + [bucket[i][j]])
                    visited[bucket[i][j]] = False

    for i in range(len(bucket)):
        for j in range(len(bucket[i])):
            visited[bucket[i][j]] = True
            comp(i, bucket[i][j], 0, [bucket[i][j]])
            visited[bucket[i][j]] = False


    return len(my_set)

print(solution(user_id, banned_id))



