def solution(n, s, a, b, fares):
    mat = [[200000001] * (n+1) for _ in range(n+1)]

    for node1, node2, w in fares:
        temp = sorted([node1, node2])
        mat[temp[0]][temp[1]] = w

    for k in range(1,n+1):
        for i in range(1, n+1):
            if k == i:
                continue
            for j in range(i+1, n+1):
                if k == j:
                    continue
                if k > j:
                    mat[i][j] = min(mat[i][k] + mat[j][k], mat[i][j])
                elif k < i:
                    mat[i][j] = min(mat[i][j], mat[k][i] + mat[k][j])
                else:
                    mat[i][j] = min(mat[i][k]+mat[k][j], mat[i][j])

    answer = 0
    if s < a:
        answer += mat[s][a]
    else:
        answer += mat[a][s]
    if s<b:
        answer += mat[s][b]
    else:
        answer += mat[b][s]
    for edge in range(1, n+1):
        if s == edge:
            continue
        if edge == a:
            if s < edge:
                if edge < b:
                    answer = min(answer, mat[s][edge] + mat[edge][b])
                else:
                    answer = min(answer, mat[s][edge] + mat[b][edge])
            else:
                if edge < b:
                    answer = min(answer, mat[edge][s] + mat[edge][b])
                else:
                    answer = min(answer, mat[edge][s] + mat[b][edge])
        elif edge == b:
            if s < edge:
                if edge < a:
                    answer = min(answer, mat[s][edge] + mat[edge][a])
                else:
                    answer = min(answer, mat[s][edge] + mat[a][edge])
            else:
                if edge < a:
                    answer = min(answer, mat[edge][s] + mat[edge][a])
                else:
                    answer = min(answer, mat[edge][s] + mat[a][edge])

        else:
            if s<edge:
                if edge<a:
                    if edge < b:
                        answer = min(answer, mat[s][edge] + mat[edge][a] + mat[edge][b])
                    else:
                        answer = min(answer, mat[s][edge] + mat[edge][a] + mat[b][edge])
                else: # a <= edge
                    if edge < b:
                        answer = min(answer, mat[s][edge] + mat[a][edge] + mat[edge][b])
                    else:
                        answer = min(answer, mat[s][edge] + mat[a][edge] + mat[b][edge])
            else:  # edge <= s
                if edge < a:
                    if edge < b:
                        answer = min(answer, mat[edge][s] + mat[edge][a] + mat[edge][b])
                    else:
                        answer = min(answer, mat[edge][s] + mat[edge][a] + mat[b][edge])
                else:  # a <= edge
                    if edge < b:
                        answer = min(answer, mat[edge][s] + mat[a][edge] + mat[edge][b])
                    else:
                        answer = min(answer, mat[edge][s] + mat[a][edge] + mat[b][edge])
    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
