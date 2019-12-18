dice_a, dice_b, dice_c, dice_d, dice_e,dice_f = 0,0,0,0,0,0
di = [None, 0, 0, -1, 1]
dj = [None,1, -1, 0, 0]
n,m,x,y,k = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]

commends = list(map(int, input().split()))

res = []
for commend in commends:
    newX, newY = x+di[commend], y+dj[commend]
    if  0<=newX<n and 0<= newY<m:
        x, y = newX, newY
        a, b, c, d, e, f = dice_a, dice_b, dice_c, dice_d, dice_e,dice_f
        if commend == 1: # 동
            dice_a, dice_b, dice_c, dice_d, dice_e,dice_f = a,e,c,f,d,b
        elif commend == 2: # 서
            dice_a, dice_b, dice_c, dice_d, dice_e,dice_f = a,f,c,e,b,d
        elif commend == 3:
            dice_a, dice_b, dice_c, dice_d, dice_e,dice_f = b,c,d,a,e,f
        else:
            dice_a, dice_b, dice_c, dice_d, dice_e,dice_f = d,a,b,c,e,f

        if mat[x][y] == 0:
            mat[x][y] = dice_d
        else:
            dice_d = mat[x][y]
            mat[x][y] = 0

        res.append(dice_b)
for r in res:
    print(r)