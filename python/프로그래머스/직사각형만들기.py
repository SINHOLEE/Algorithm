def solution(v):
    v = sorted(v)
    x_dic = {}
    y_dic = {}
    for x, y in v:
        if x_dic.get(x) is None:
            x_dic[x] = 1
        else:
            x_dic[x] += 1
        if y_dic.get(y) is None:
            y_dic[y] = 1
        else:
            y_dic[y] += 1

    answer = []
    for x, cnt in x_dic.items():
        if cnt == 1:
            answer.append(x)
            break
    for y, cnt in y_dic.items():
        if cnt == 1:
            answer.append(y)
    return answer


print(solution([[1, 1], [2, 2], [1, 2]]))
