T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    containers_weight = sorted(list(map(int, input().split())))[::-1]
    trucks_carriable_weight = sorted(list(map(int, input().split())))[::-1]

    # print(containers_weight)
    # print(trucks_carriable_weight)
    truck_visited = [False] * len(trucks_carriable_weight)
    ans = 0
    for container in containers_weight:
        for truck in range(len(trucks_carriable_weight)-1, -1, -1):
            if truck_visited[truck] == False and container <= trucks_carriable_weight[truck]:
                ans += container
                truck_visited[truck] = True
                break
    print('#%s %s' % (tc, ans))