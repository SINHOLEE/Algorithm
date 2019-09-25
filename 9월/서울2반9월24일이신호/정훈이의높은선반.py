def combi(depth, k, rr, result):
    global bigger_than_B_but_min_result, B, N, count,check
    count += 1
    if B <= result:
        if result < bigger_than_B_but_min_result:
            bigger_than_B_but_min_result = result
        check = True
        return
    if depth == rr:
        return


    for i in range(k, N):
        if visited[i] == False:
            visited[i] = True
            combi(depth+1, i+1, r, result+heights[i])
            visited[i] = False
T = int(input())


for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    count = 0
    check = False
    # print(heights)
    bigger_than_B_but_min_result = 1000000000000000000000000000
    for r in range(N, -1, -1):
        if check:
            break
        visited = [False] * N
        combi(0, 0, r, 0)
    print('#%s %s' % (tc, bigger_than_B_but_min_result - B))
    # print(count)