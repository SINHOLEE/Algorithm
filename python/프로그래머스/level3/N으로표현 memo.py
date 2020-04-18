from pprint import pprint
cache={}


# 남아있는 숫자를 사칙연산으로 통해 표현할 수 있는 제일 적은 갯수 반환
def rec(leave, leaveCnt, N, number):
    if leave in cache.keys():
        return cache[leave]
    if leave==0:
            return 0

    if leave not in cache:
        cache[leave]=9
   
    minCnt=cache[leave]
    acc = number - leave
    num = 0
    for i in range(leaveCnt):
        num= num * 10 + N
        newLeaveCnt=leaveCnt-(i+1)
        candiCnt = rec(number - (acc + num), newLeaveCnt, N, number)
        if minCnt > candiCnt + (i + 1):
            minCnt = candiCnt + (i + 1)
        candiCnt = rec(number-(acc-num), newLeaveCnt, N, number)
        if minCnt > candiCnt + (i + 1):
            minCnt = candiCnt + (i + 1)
        candiCnt = rec(number - acc * num, newLeaveCnt, N, number)
        if minCnt>candiCnt+(i+1):
            minCnt=candiCnt+(i+1)
        candiCnt = rec(number - acc // num, newLeaveCnt, N, number)
        if minCnt > candiCnt + (i + 1):
            minCnt = candiCnt + (i + 1)


    cache[leave]=minCnt
    return minCnt


def solution(N, number):
    rec(number,8, N, number)
    print(cache)
    return -1 if cache[number]>8 else cache[number]


print(solution(9, 72))
