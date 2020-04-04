def solution(n, results):
    mat = [[0] * (n+1) for _ in range(n+1)]
    for items in results:
        mat[items[0]][items[1]] = 1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if mat[i][k] and mat[k][j]:
                    mat[i][j] = 1

    answer = 0
    res = [0] * (n+1)
    for i in range(1, n+1):
        res[i] = sum(mat[i])
        for j in range(1, n+1):
            res[i] += mat[j][i]

    for r in res:
        if r == n-1:
            answer += 1
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
