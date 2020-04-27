def solution(dartResult):
    res = []
    flag = False
    for i in range(len(dartResult)):
        if flag:
            flag = False
            continue
        if dartResult[i] == "S":
            pass
        elif dartResult[i] == "D":
            res[-1] = res[-1] ** 2
        elif dartResult[i] == "T":
            res[-1] = res[-1] ** 3
        elif dartResult[i] == "*":
            if len(res) == 1:
                res[-1] = res[-1] * 2
            elif len(res) > 1:
                res[-1] = res[-1] * 2
                res[-2] = res[-2] * 2
        elif dartResult[i] == "#":
            res[-1] = res[-1] * -1
        else:
            if i+1 < len(dartResult) and dartResult[i:i+2] == "10":
                res.append(int(dartResult[i:i+2]))
                flag = True
            else:
                res.append(int(dartResult[i]))
    answer = sum(res)
    return answer


solution('1D*2S*10S*')
