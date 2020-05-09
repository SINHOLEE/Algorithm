def solution(gems):
    answer = []
    gems_set = set(gems)
    dic = {}
    last = len(gems) # 8 이제 구간으로 생각한다. ex) 0~1 -> 0, 7~8 -> 7
    # two point
    s = 0
    e = 0
    min_value = 9876544321
    my_set = set()
    while True:
        if my_set == gems_set:
            dic[gems[s]] -= 1
            if dic[gems[s]] == 0:
                my_set.remove(gems[s])
            s += 1
        elif e == last:
            break
        else:
            if dic.get(gems[e]) is None:
                dic[gems[e]] = 1
                my_set.add(gems[e])
            else:
                dic[gems[e]] += 1
                my_set.add(gems[e])

            e += 1

        if my_set == gems_set:
            if e-s < min_value:
                answer = [s+1, e]
                min_value = e-s
    return answer


solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])

