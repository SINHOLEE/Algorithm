visited = [False] * 32
        #                                                    19 20  21 22 23 24 25 26 27 28 29 30 31
board = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38, 13,16,19,25,22,24,28,27,26,30,35,40]
five_list = [5,20,21,22,23,29,30,31] #1 index 7
teen_list = [10,24,25,23,29,30,31] #2 index 6
fifteen_list = [15,26,27,28,23,29,30,31] #3 index7

def move(sum_scores, a, b, c, d, num_of_dice, an,bn,cn,dn):
    global max_total


    if num_of_dice == 10:

        if max_total < sum_scores:
            if sum_scores == 190 or sum_scores == 193:
                print(sum_scores, a, b, c, d, num_of_dice, an, bn, cn, dn)
            max_total = sum_scores
        return
    k = dices[num_of_dice]
    # 첫번째 말
    if an == 0:
        if a + k > 19:
            if a + k == 20 and visited[31] == False:
                visited[a] = False
                a = 31
                visited[31] = True
                move(sum_scores+40, 7,b,c,d,num_of_dice+1, 3,bn,cn,dn )
                visited[31] = False
            else:
                visited[a] = False
                move(sum_scores, a, b, c, d, num_of_dice+1, 4, bn,cn, dn)
                visited[a] = True

        elif a + k == 5 and visited[a + k] == False:
            visited[a + k] = True
            visited[a] = False
            move(sum_scores + 10, 0, b,c,d,num_of_dice+1, 1,bn,cn,dn)
            visited[a + k] = False

        elif a + k == 10 and visited[a + k] == False:
            visited[a + k] = True
            visited[a] = False
            move(sum_scores + 20, 0, b, c, d, num_of_dice + 1, 2, bn, cn, dn)
            visited[a + k] = False
        elif a + k == 15 and visited[a + k] == False:
            visited[a + k] = True
            visited[a] = False
            move(sum_scores + 30, 0, b, c, d, num_of_dice + 1, 3, bn, cn, dn)
            visited[a + k] = False
        else:
            if visited[a+k] == False:
                visited[a + k] = True
                visited[a] = False
                move(sum_scores + board[a+k], a+k, b, c, d, num_of_dice + 1, 0, bn, cn, dn)
                visited[a + k] = False
    elif an == 1:
        if a + k > 7:
            visited[five_list[a]] = False
            move(sum_scores, a, b, c, d, num_of_dice + 1, 4, bn, cn, dn)
            visited[five_list[a]] = True
        else:
            if visited[five_list[a+k]] == False:
                visited[five_list[a+k]] = True
                visited[five_list[a]] = False
                move(sum_scores + board[five_list[a+k]], a+k, b, c, d, num_of_dice + 1, 1, bn, cn, dn)
                visited[five_list[a + k]] = False
    elif an == 2:
        if a + k > 6:
            visited[teen_list[a]] = False
            move(sum_scores, a, b, c, d, num_of_dice + 1, 4, bn, cn, dn)
            visited[teen_list[a]] = True
        else:
            if visited[teen_list[a+k]] == False:
                visited[teen_list[a+k]] = True
                visited[teen_list[a]] = False

                move(sum_scores + board[teen_list[a+k]], a+k, b, c, d, num_of_dice + 1, 2, bn, cn, dn)
                visited[teen_list[a + k]] = False
    elif an == 3:
        if a + k > 7:
            visited[fifteen_list[a]] = False
            move(sum_scores, a, b, c, d, num_of_dice + 1, 4, bn, cn, dn)
            visited[fifteen_list[a]] = True
        else:
            if visited[fifteen_list[a+k]] == False:
                visited[fifteen_list[a+k]] = True
                visited[fifteen_list[a]] = False

                move(sum_scores + board[fifteen_list[a+k]], a+k, b, c, d, num_of_dice + 1, 3, bn, cn, dn)
                visited[fifteen_list[a + k]] = False
    else:
        pass

    # 두번째
    if bn == 0:
        if b + k > 19:
            if b + k == 20 and visited[31] == False:
                visited[b] = False
                b = 31
                visited[31] = True
                move(sum_scores+40, a,7,c,d,num_of_dice+1, an,3,cn,dn )
                visited[31] = False
            else:
                visited[b] = False
                move(sum_scores, a, b, c, d, num_of_dice+1, an, 4,cn, dn)
                visited[b] = True

        elif b + k == 5 and visited[b + k] == False:
            visited[b + k] = True
            visited[b] = False
            move(sum_scores + 10, a, 0,c,d,num_of_dice+1, an,1,cn,dn)
            visited[b + k] = False
        elif b + k == 10 and visited[b + k] == False:
            visited[b + k] = True
            visited[b] = False
            move(sum_scores + 20, a, 0, c, d, num_of_dice + 1, an, 2, cn, dn)
            visited[b + k] = False
        elif b + k == 15 and visited[b + k] == False:
            visited[b] = False
            visited[b + k] = True
            move(sum_scores + 30, a, 0, c, d, num_of_dice + 1, an, 3, cn, dn)
            visited[b + k] = False
        else:
            if visited[b+k] == False:
                visited[b + k] = True
                visited[b] = False
                move(sum_scores + board[b+k], a, b+k, c, d, num_of_dice + 1, an, 0, cn, dn)
                visited[b + k] = False
    elif bn == 1:
        if b + k > 7:
            visited[five_list[b]] = False
            move(sum_scores, a, b, c, d, num_of_dice + 1, an, 4, cn, dn)
            visited[five_list[b]] = True
        else:
            if visited[five_list[b+k]] == False:
                visited[five_list[b+k]] = True
                visited[five_list[b]] = False
                move(sum_scores + board[five_list[b+k]], a, b+k, c, d, num_of_dice + 1, an, 1, cn, dn)
                visited[five_list[b + k]] = False
    elif bn == 2:
        if b + k > 6:
            visited[teen_list[b]] = False
            move(sum_scores, a, b, c, d, num_of_dice + 1, an, 4, cn, dn)
            visited[teen_list[b]] = True
        else:
            if visited[teen_list[b+k]] == False:
                visited[teen_list[b+k]] = True
                visited[teen_list[b]] = False
                move(sum_scores + board[teen_list[b+k]], a, b+k, c, d, num_of_dice + 1, an, 2, cn, dn)
                visited[teen_list[b + k]] = False
    elif bn == 3:
        if b + k > 7:
            visited[fifteen_list[b]] = False
            move(sum_scores, a, b, c, d, num_of_dice + 1, an, 4, cn, dn)
            visited[fifteen_list[b]] = True
        else:
            if visited[fifteen_list[b+k]] == False:
                visited[fifteen_list[b+k]] = True
                visited[fifteen_list[b]] = False
                move(sum_scores + board[fifteen_list[b+k]], a, b+k, c, d, num_of_dice + 1, an, 3, cn, dn)
                visited[fifteen_list[b + k]] = False

    # 세번째 말
    if cn == 0:
        if c + k > 19:
            if c + k == 20 and visited[31] == False:
                visited[c] = False
                c = 31
                visited[31] = True
                move(sum_scores+40, a,b,7,d,num_of_dice+1, an,bn,3,dn )
                visited[31] = False
            else:
                visited[c] = False
                move(sum_scores, a, b, c, d, num_of_dice+1, an, bn,1, dn)
                visited[c] = True
        elif c + k == 5 and visited[c + k] == False:
            visited[c + k] = True
            visited[c] = False
            move(sum_scores + 10, a, b,0,d,num_of_dice+1, an,bn,1,dn)
            visited[c + k] = False

        elif c + k == 10 and visited[c + k] == False:
            visited[c + k] = True
            visited[c] = False
            move(sum_scores + 20, a, b, 0, d, num_of_dice + 1, an, bn, 2, dn)
            visited[c + k] = False
        elif c + k == 15 and visited[c + k] == False:
            visited[c + k] = True
            visited[c] = False
            move(sum_scores + 30, a, b, 0, d, num_of_dice + 1, an, bn, 3, dn)
            visited[c + k] = False
        else:
            if visited[c+k] == False:
                visited[c + k] = True
                visited[c] = False
                move(sum_scores + board[c+k], a, b, c+k, d, num_of_dice + 1, an, bn, 0, dn)
                visited[c + k] = False
    elif cn == 1:
        if c + k > 7:
            visited[five_list[c]] = False
            move(sum_scores, a, b, c, d, num_of_dice + 1, an, bn, 4, dn)
            visited[five_list[c]] = True
        else:
            if visited[five_list[c+k]] == False:
                visited[five_list[c+k]] = True
                visited[five_list[c]] = False
                move(sum_scores + board[five_list[c+k]], a, b, c+k, d, num_of_dice + 1, an, bn, 1, dn)
                visited[five_list[c + k]] = False
    elif cn == 2:
        if c + k > 6:
            visited[teen_list[c]] = False
            move(sum_scores, a, b, c, d, num_of_dice + 1, an, bn, 4, dn)
        else:
            if visited[teen_list[c+k]] == False:
                visited[teen_list[c+k]] = True
                visited[teen_list[c]] = False
                move(sum_scores + board[teen_list[c+k]], a, b, c+k, d, num_of_dice + 1, an, bn, 2, dn)
                visited[teen_list[c + k]] = False
    elif cn == 3:
        if c + k > 7:
            visited[fifteen_list[c]] = False
            move(sum_scores, a, b, c, d, num_of_dice + 1, an, bn, 4, dn)
            visited[fifteen_list[c]] = True
        else:
            if visited[fifteen_list[c+k]] == False:
                visited[fifteen_list[c+k]] = True
                visited[fifteen_list[c]] = False
                move(sum_scores + board[fifteen_list[c+k]], a, b, c+k, d, num_of_dice + 1, an, bn, 3, dn)
                visited[fifteen_list[c + k]] = False

    # 네번째 말
    if dn == 0:
        if d + k > 19:
            if d + k == 20 and visited[31] == False:
                visited[d] = False
                d = 31
                visited[31] = True
                move(sum_scores + 40, a, b, c, 7, num_of_dice + 1, an, bn, cn, 3)
                visited[31] = False
            else:
                visited[d] = False
                move(sum_scores, a, b, c, d, num_of_dice + 1, an, bn, cn, 4)
                visited[d] = True

        elif d + k == 5 and visited[d + k] == False:
            visited[d + k] = True
            visited[d] = False
            move(sum_scores + 10, a, b,c,0,num_of_dice+1, an,bn,cn,1)
            visited[d + k] = False

        elif d + k == 10 and visited[d + k] == False:
            visited[d] = False
            visited[d + k] = True
            move(sum_scores + 20, a, b, c, 0, num_of_dice + 1, an, bn, cn, 2)
            visited[d + k] = False
        elif d + k == 15 and visited[d + k] == False:
            visited[d + k] = True
            visited[d] = False
            move(sum_scores + 30, a, b, c, 0, num_of_dice + 1, an, bn, cn, 3)
            visited[d + k] = False
        else:
            if visited[d+k] == False:
                visited[d + k] = True
                visited[d] = False
                move(sum_scores + board[d+k], a, b, c, d+k, num_of_dice + 1, an, bn, cn, 0)
                visited[d + k] = False
    elif dn == 1:
        if d + k > 7:
            visited[five_list[d]] = False
            move(sum_scores, a, b, c, d, num_of_dice + 1, an, bn, cn, 4)
            visited[five_list[d]] = True

        else:
            if visited[five_list[d+k]] == False:
                visited[five_list[d+k]] = True
                visited[five_list[d]] = False
                move(sum_scores + board[five_list[d+k]], a, b, c, d+k, num_of_dice + 1, an, bn, cn, 1)
                visited[five_list[d + k]] = False
    elif dn == 2:
        if d + k > 6:
            visited[teen_list[d]] = False
            move(sum_scores, a, b, c, d, num_of_dice + 1, an, bn, cn, 4)
        else:
            if visited[teen_list[d+k]] == False:
                visited[teen_list[d+k]] = True
                visited[teen_list[d]] = False
                move(sum_scores + board[teen_list[d+k]], a, b, c, d+k, num_of_dice + 1, an, bn, cn, 2)
                visited[teen_list[d + k]] = False
    elif dn == 3:
        if d + k > 7:
            visited[fifteen_list[d]] = False
            move(sum_scores, a, b, c, d, num_of_dice + 1, an, bn, cn, 4)
            visited[fifteen_list[d]] = True
        else:
            if visited[fifteen_list[d+k]] == False:
                visited[fifteen_list[d+k]] = True
                visited[fifteen_list[d]] = False
                move(sum_scores + board[fifteen_list[d+k]], a, b, c, d+k, num_of_dice + 1, an, bn, cn, 3)
                visited[fifteen_list[d + k]] = False


dices = list(map(int, input().split()))

max_total = 0
move(0, 0, 0, 0, 0, 0, 0,0,0,0)
print(max_total)