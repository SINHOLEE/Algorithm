from pprint import pprint


def solution(words):
    answer = 0
    dic = {}
    for word in words:
        temp = dic
        for ch in word:
            if temp.get(ch) is None:
                temp[ch] = {'num' : 1}
            else:
                temp[ch]['num'] += 1
            temp = temp[ch]
        temp['end'] = {'num': 1}
    # search
    for word in words:
        cnt = 1
        temp = dic
        for ch in word:
            if temp[ch]['num'] == 1:
                answer += cnt
                break
            cnt+=1
            temp = temp[ch]
        else:
            if temp['end']['num'] == 1:
                answer += cnt-1
    return answer


solution(	["go", "gone", "guild"])
