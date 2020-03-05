dartResult = '1D2S0T'


def solution(dartResult):
    scores = [0, 0, 0]
    i = 0
    dart_idx = 0
    temp = 0

    while True:
        if dart_idx >= len(dartResult):
            break
        if dartResult[dart_idx] in {'0','1','2','3','4','5','6','7','8','9','10'}:
            if dartResult[dart_idx] == '1' and dartResult[dart_idx+1] == '0':
                temp = 10
                dart_idx += 1
            else:
                temp += int(dartResult[dart_idx])
            dart_idx += 1
            continue
        elif dartResult[dart_idx] in {'S', 'D', 'T'}:
            if dartResult[dart_idx] == 'D':
                temp = temp ** 2
            elif dartResult[dart_idx] == 'T':
                temp = temp ** 3
            scores[i] = temp
            i += 1
            dart_idx += 1
            temp = 0
            continue
        else:
            if dartResult[dart_idx] == '*':
                if i == 1:
                    scores[i-1] = scores[i-1] * 2
                else:
                    scores[i-2] = (scores[i-2] * 2)
                    scores[i-1] = (scores[i-1] * 2)
            elif dartResult[dart_idx] == '#':
                scores[i-1] =(scores[i-1] * -1)
            dart_idx+= 1

    answer = 0
    return sum(scores)

print(solution(dartResult))