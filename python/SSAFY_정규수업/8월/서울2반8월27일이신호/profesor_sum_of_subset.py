T = int(input())


# 단계별로 값을 누적하여 누적한 값이 최소값보다 같거나 크면 다음단계로 안내려감.
def find_min(row):
    global mymin
    global submin
    if submin > mymin:
        return
    if row == n:
        if submin < mymin:
            mymin = submin
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            submin += mymap[row][i]  # 최소값 누적변수에 누적
            find_min(row + 1)
            submin -= mymap[row][i]  # 들어갔다 나왔으니 누적 숫자만큼 뺌
            visited[i] = 0

for tc in range(1, T+1):
    n = int(input())
    mymap = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n

    mymin = 99999999999999
    submin = 0
    find_min(0)
    print('#{} {}'.format(tc, mymin))
