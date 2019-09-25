import copy

# tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO'], ['SFO', 'ATL']]
def solution(tickets):
    global answer1

    answer = []
    tickets = sorted(tickets,key=lambda x: x[-1])
    # print(tickets)
    lens = len(tickets)
    visited = [False] * len(tickets)
    answer1 = []
    ans=[]
    def DFS( depth, answer):
        global answer1
        if lens  == depth:
            if not answer1:
                answer1 = answer[:]
            return
        for j in range(lens):
            if visited[j] == False and answer[-1] == tickets[j][0]:
                visited[j] = True
                DFS(depth+1, answer + [tickets[j][1]])
                visited[j] = False

    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            ans.append(tickets[i][0])
            DFS(0, ans)
            ans = []

        # print(ans)

    return answer1

print(solution(tickets))
