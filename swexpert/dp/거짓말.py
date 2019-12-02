n, m = map(int, input().split())
temp = list(map(int, input().split()))
people = [[] for _ in range(n+1)]
known = temp[1:]
people_visited = [0] *(n+1)
partys = []
for i in range(m):
    temp = list(map(int, input().split()))
    partys.append(temp[1:])
    for p in temp[1:]:
        people[p].append(i)
if len(known) == 0:
    pass
else:
    people_visited[known[0]] = 1
    while known:
        u = known.pop(0)
        for party_num in people[u]:
            for v in partys[party_num]:
                if people_visited[v] == 0:
                    people_visited[v] = 1
                    known.append(v)

cnt = 0
for party in partys:
    for v in party:
        if people_visited[v] == 1:
            break
    else:
        cnt += 1
print(cnt)
