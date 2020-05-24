import sys
sys.setrecursionlimit(100001)


def solution(total_sp, skills):
    global adj_list

    def post_order(node):
        global skills, adj_list
        if len(adj_list[node]) == 0:
            visited[node] = 1
            return 1
        for nxt in adj_list[node]:
            visited[node] += post_order(nxt)
        return visited[node]

    len_skills = len(skills)
    adj_list = [[] for _ in range(len_skills+2)]
    visited = [0] * (len_skills + 2)
    indegree = [0] * (len_skills + 2)
    for a, b in skills:
        adj_list[a].append(b)
        indegree[b] = 1
    # root를 찾아라
    for i in range(1, len_skills+2):
        if indegree[i] == 0:
            root = i
            break
    post_order(root)

    d = sum(visited)
    sub = int(total_sp / d)
    answer = list(map(lambda x: x * sub, visited))
    return answer[1:]


print(solution(121, [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]))


