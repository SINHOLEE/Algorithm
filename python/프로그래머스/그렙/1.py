def solution(day, k):
    answer = [0] * 12
    cal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = 1
    m = 1
    for i in range(365):
        if d ==k:
            if day == 5 or day == 6:
                answer[m-1] = 1
            else:
                answer[m-1] = 0
        d+=1
        day+=1
        if day == 7:
            day = 0
        if d > cal[m - 1]:
            m+=1
            d = 1
    return answer


solution(6, 1)