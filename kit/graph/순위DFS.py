from pprint import pprint

n = 7
results = [[1, 2], [4, 2], [1, 5], [2, 3],[5,3],[5,6],[3,6],[3,7],[6,7]]


def dfs(matrix, loser, winner):
    for i, j in enumerate(matrix[loser]):
        if j == loser:
            matrix[winner][i] = winner
            matrix[i][winner] = winner


def solution(n, results):
    # 1. 2x2 matrix 만들기 (알 수 없는 경우는 0)
    matrix = [[0]*(n+1) for _ in range(n+1)]

    # 2. 각 경기 결과에 대해서 진 선수가 이긴 선수를 탐색해서 matrix를 채우기
    for result in results:
        winner = result[0]
        loser = result[1]
        matrix[winner][loser] = winner
        matrix[loser][winner] = winner
    pprint(matrix)
    for _ in range(2):
        for winner in range(1,n+1):
            for loser in range(1,n+1):
                if winner == matrix[winner][loser]:
                    dfs(matrix, loser, winner)

    answer = 0
    print(    )
    pprint(matrix)
    for i in range(1, n+1):
        count_zero = 0
        for j in range(1, n+1):
            if matrix[i][j] == 0:
                count_zero += 1
        if count_zero == 1:
            answer += 1

    return answer

print(solution(n, results))