def solution(gems):
    def check(dic):
        a = set()
        for key, value in dic.items():
            if value > 0:
                a.add(key)
        return a

    answer = []
    gems_set = set(gems)
    dic = {}
    last = len(gems) # 8 이제 구간으로 생각한다. ex) 0~1 -> 0, 7~8 -> 7
    # two point
    s = 0
    e = 0
    min_value = 9876544321
    while True:
        if s > e:
            break
        if check(dic) == gems_set:

            dic[gems[s]] -= 1
            s += 1
        elif e == last:
            break
        else:
            if dic.get(gems[e]) is None:
                dic[gems[e]] = 1
            else:
                dic[gems[e]] += 1
            e += 1
        if check(dic) == gems_set:
            if e-s < min_value:
                answer = [s+1, e]
                min_value = e-s
    return answer