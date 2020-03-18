for t in range(1, int(input())+1):
    hashmap1 = {}
    hashmap2 = {}
    trees = []
    for i in range(2):
        trees.append(input())
    a = ""
    a_cnt = 0
    b = ""
    b_cnt = 0
    for j in range(len(trees[0])+1):
        # 1
        if a !="" and a_cnt == 0:
            if hashmap1.get(a) is not None:
                hashmap1[a] += 1
                hashmap1["".join(map(str, map(lambda x:str(0) if x == "1" else str(1), a[::-1])))] += 1
            else:
                hashmap1[a] = 1
                hashmap1["".join(map(str, map(lambda x:str(0) if x == "1" else str(1), a[::-1])))] = 1
            a = ""
        if j == len(trees[0]):
            break
        if trees[0][j] == "1":
            a_cnt -= 1
        else:
            a_cnt += 1
        a += trees[0][j]

    for j in range(len(trees[0])+1):
        # 1
        if b !="" and b_cnt == 0:
            if hashmap2.get(b) is not None:
                hashmap2[b] += 1
                hashmap2["".join(map(str, map(lambda x:str(0) if x == "1" else str(1), b[::-1])))] += 1
            else:
                hashmap2[b] = 1
                hashmap2["".join(map(str, map(lambda x:str(0) if x == "1" else str(1), b[::-1])))] = 1
            b = ""
        if j == len(trees[0]):
            break
        if trees[1][j] == "1":
            b_cnt -= 1
        else:
            b_cnt += 1
        b += trees[1][j]

    if hashmap1 == hashmap2:
        print(1)
    else:
        print(0)