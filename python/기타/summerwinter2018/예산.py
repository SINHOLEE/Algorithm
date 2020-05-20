

def solution(d, budget):
    d.sort()
    answer = 0
    for money in d:
        budget -= money
        if budget >= 0:
            answer+=1
    return answer
solution([1, 3, 2, 5, 4], 9)
solution([2, 2, 3, 3], 10)
solution([1,2,6,9], 10)