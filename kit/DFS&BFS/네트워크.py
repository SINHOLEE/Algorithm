n = 3
computers = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]



def solution(n, computers):
    visited =[False] * n

    def DFS(node):
        visited[node] = True

        for i in range(n):
            if visited[i] == False and computers[node][i] == 1 and i != node:
                DFS(i)
    count = 0
    for i in range(n):
        if visited[i] == False:
            DFS(i)
            count += 1

    return count

print(solution(n, computers))