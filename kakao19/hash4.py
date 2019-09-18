keys_dic = {}
dic = {}
def divied_sort(k):
    if len(k) <= 1:
        return k

    else:
        mid = len(k) // 2

        left = divied_sort(k[:mid])
        right = divied_sort(k[mid:])

        return merge(left, right)

def merge(lef1, rig1):
    global keys_dic

    new_list = []
    while True:
        if len(lef1) == 0 or len(rig1) == 0:
            break
        if keys_dic[lef1[0]] < keys_dic[rig1[0]]:
            aaa = lef1.pop(0)
            new_list.append(aaa)
        else:
            aaa = rig1.pop(0)
            new_list.append(aaa)

    while True:
        if len(lef1) == 0:
            break
        aaa = lef1.pop(0)
        new_list.append(aaa)

    while True:
        if len(rig1) == 0:
            break
        aaa = rig1.pop(0)
        new_list.append(aaa)
    return new_list











# genres = ["classic", "pop", "classic", "classic", "pop", ]
# plays = [500, 600, 150, 800, 2500,]
def solution(genres, plays):

    global keys_dic
    for id in range(len(genres)):
        if genres[id] in dic:
            dic[genres[id]].append((id, plays[id]))
        else:
            dic[genres[id]] =[(id, plays[id])]
    keys = list(dic.keys())
    # print(dic)
    for k in keys:
        for i in dic[k]:
            if k in keys_dic:

                keys_dic[k] += i[1]
            else:
                keys_dic[k] = i[1]
    keys = divied_sort(keys)[::-1]
    # print(keys)
    # print(keys_dic)
    id = []
    for k in keys:
        aa = dic[k]
        # print(aa)
        if len(aa) == 1:
            pass
        else:
            for jj in range(len(aa)-1):
                for kk in range(jj+1, len(aa)):

                    if aa[jj][1] < aa[kk][1]:
                        aa[jj], aa[kk] = aa[kk], aa[jj]
                    elif aa[jj][1] == aa[kk][1]:
                        if aa[jj][0] < aa[kk][0]:
                            pass
                        else:
                            aa[jj], aa[kk] = aa[kk], aa[jj]

                    else:
                        pass
        # print(aa)
        temp = aa[:2]
        # print(temp)
        for tem in temp:
            id.append(tem[0])
        # print(temp)
        # id.extend(aa[:2][0])

    # print(id)


    return id

