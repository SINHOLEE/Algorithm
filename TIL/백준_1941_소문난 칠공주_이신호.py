

di = [0,0,-1,1]
dj = [-1,1,0,0]
def check(my_combi):
    a = my_combi[0]
    visisted = [0] * 7
    visisted[0] = 1
    cnt = 1
    q = [(a[1], a[2])]
    while q:
        a = q.pop(0)
        x,y = a[0], a[1]
        for k in range(4):
            newX,newY = x+di[k], y+dj[k]
            for j in range(7):
                if visisted[j]:
                    continue
                people,xx,yy  = my_combi[j][0], my_combi[j][1],my_combi[j][2]
                if xx == newX and yy == newY:
                    q.append((xx, yy))
                    visisted[j] = 1
                    cnt+=1
    if cnt == 7:
        return 1
    else:
        return 0
lis = []
for i in range(5):
    temp = list(input())
    for j in range(5):
        if temp[j] == "S":
            lis.append((0, i, j))
        else:
            lis.append((1, i, j))
total_cnt = 0
for a in range(25):
    for b in range(a+1,25):
        for c in range(b+1, 25):
            for d in range(c+1,25):
                for e in range(d+1, 25):
                    for f in range(e+1,25):
                        for g in range(f+1, 25):
                            if sum((lis[a][0],lis[b][0],lis[c][0],lis[d][0],lis[e][0],lis[f][0],lis[g][0])) >3:
                                continue
                            total_cnt += check([lis[a],lis[b],lis[c],lis[d],lis[e],lis[f],lis[g]])

print(total_cnt)