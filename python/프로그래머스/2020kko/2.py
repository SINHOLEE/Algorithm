'''
30분컷
'''

dic = {}

def solution(orders, course):
    for num in course:
        dic[num] = {'max':0}

    def combi(depth, res, i):
        if depth == num:
            target = "".join(sorted(res))
            if dic[num].get(target) is None:
                dic[num][target] = 1
                dic[num]['max'] = max(dic[num]['max'], 1)
            else:
                dic[num][target] += 1
                dic[num]['max'] = max(dic[num]['max'], dic[num][target])
            return
        for j in range(i, order_len):
            if visited[j]:
                continue
            visited[j] = 1
            combi(depth+1, res + [order[j]], j)
            visited[j] = 0

    for order in orders:
        order_len = len(order)
        visited = [0] * order_len
        for num in course:
            if len(order) < num:
                continue
            combi(0, [], 0)
    answer = []
    for k, v in dic.items():
        if v["max"] >= 2:
            max_cnt = v["max"]
            for order, cnt in v.items():
                if order != "max" and cnt == max_cnt:
                    answer.append(order)
    answer.sort()

    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
