# 33분 소요
# 1. 순환 리스트에서 총 초밥의 개수보다 작은 k개의 연속되는 다른 초밥을 먹을 경우 할인을 받는다.
# 2. 구하고 싶은 것, 손님이 먹을 수 있는 최대 가짓수!
from github_com.SINHOLEE.my_modules.memory import memory_check


@memory_check
def solution():
    n, d, k, c = map(int, input().split())
    sushi = []
    for i in range(n):
        sushi.append(int(input()))
    res = 0
    for i in range(n):
        temp = set()
        for j in range(k):
            temp.add(sushi[(i+j)%n])
        if c in temp:
            res = max(res, len(temp))
        else:
            res = max(res, len(temp)+1)
    print(res)


solution()




