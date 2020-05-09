def solution(n, path, order):
    answer = False
    adj_list = [[] for _ in range(n)]
    for a, b in path:
        adj_list[a].append(b)
        adj_list[b].append(a)


    return answer


solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]])
