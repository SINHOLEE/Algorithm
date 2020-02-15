dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

for t in range(1, int(input())+1):
    k = int(input())
    dic = {}
    for _ in  range(k):
        x, y, d, e = map(int, input().split())
        if dic.get((y*2,x*2)) == None:
            dic[(y*2, x*2)] = [(d, e)]

    res = 0
    while dic:
        new_dic = {}
        for key, item in dic.items():
            yy, xx = key[0], key[1]
            dd, ee = item[0][0], item[0][1]
            yyy,xxx = yy+dy[dd], xx+dx[dd]
            if not(-2001<=yyy<=2001 and -2001<=xxx<=2001):
                continue
            if new_dic.get((yyy,xxx)) == None:
                new_dic[(yyy,xxx)] = [(dd, ee)]
            else:
                new_dic[(yyy,xxx)].append((dd,ee))

        fordellist = []
        for key1, item1 in new_dic.items():
            if len(item1) > 1:
                fordellist.append(key1)
                res += sum(map(lambda x : x[1], item1))

        for delkey in fordellist:
            del new_dic[delkey]
        dic = new_dic
    print('#%s %s' % (t, res))