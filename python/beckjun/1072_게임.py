import random

def solution(x,y):
    target = ((y*100)//x)
    s = y
    e = 2000000000
    answer = -1
    while s<=e:
        m = (s+e)//2
        if target < (((m)*100) //(x+m-y)):
            answer=m-y
            e = m-1
        else:
            s = m+1
    return answer


def solution2(x,y):
    target = ((y*100)//x)

    s = 0
    e = x
    answer = -1
    while s<=e:
        m = (s+e)//2
        # print('22222:', y+m, x+m,((y+m)*100) //(x+m),m)
        if target < (((y+m)*100) //(x+m)):
            answer=m
            e = m-1
        else:
            s = m+1
    return answer

if __name__ == '__main__':
    # x,y = map(int, input().split())
    for _ in range(1000):
        x,y = random.randint(1,1000000000),random.randint(1,1000000000)
        if(y<x):
            if(solution(x,y) != solution3(x,y) ):
                print(x,y, solution(x,y), solution3(x,y))
    # print(solution(100, 97),solution2(100, 97))