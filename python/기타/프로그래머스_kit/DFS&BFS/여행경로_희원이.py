def dfs(num, tickets, visited, airport, airport_num):
    global answer
    if num == airport_num:
        if len(answer) == 1:
            answer = airport[:]

        return
    for i in range(airport_num):
        if tickets[i][0] == airport[-1] and not visited[i]:
            visited[i] = True
            dfs(num + 1, tickets, visited, airport + [tickets[i][1]], airport_num)
            visited[i] = False

def solution(tickets):
    global answer
    answer = ['ICN']
    n = len(tickets)
    # tickets = sorted(tickets,key=lambda x: x[-1])

    visited = [False] * n
    dfs(0, tickets, visited, ['ICN'], n)
    return answer