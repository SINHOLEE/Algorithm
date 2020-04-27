
def sub_solution(w):
    global static_card
    word_dic = {}
    for chrr in w:
        if word_dic.get(chrr) is None:
            word_dic[chrr] = 1
        else:
            word_dic[chrr] += 1
    cnt = 0
    for i in range(3):
        flag = False
        for c1 in static_card[i]:
            if c1 in word_dic.keys():
                if not flag:
                    flag = True
                    cnt += 1
                word_dic[c1] -= 1
    # print(word_dic)
    # print(cnt)
    for k, item in word_dic.items():
        if item > 0:
            return False
    else:
        if cnt == 3:
            return True
    return False


def solution(card, word):
    global static_card
    static_card = card
    answer = []
    for w in word:
        if sub_solution(w):
            answer.append(w)
    if len(answer) == 0:
        return ['-1']
    return answer


static_card = []
print(solution(	["ABACDEFG", "NOPQRSTU", "HIJKLKMM"], ["GPQM", "GPMZ", "EFU", "MMNA"]))

