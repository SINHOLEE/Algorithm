# dic1 = {1:1, 2:2}
# dic2 = {3:3, 4:4}
#
# dic1.update(dic2)
# print(dic2)
DEBUG=False
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
T = int(input())
for t in range(1, T+1):
    n, m, k = map(int,input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]

    board = {}
    cells = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] !=0:
                board[(i, j)] = [mat[i][j], 0, 0]
                cells += 1
    dead_board = {}
    deal_cells = 0
    for _ in range(k): # k 번 만큼 반복

        # step1
        temp_board = {}
        new_board = {}
        for xy , lis in board.items():
            x, y = xy[0], xy[1]
            life, off_point, on_point = lis[0], lis[1], lis[2]

            if life == on_point == off_point: # 죽었으면, 아무것도 안하고 패스
                dead_board[(x,y)] = [life,off_point,on_point]
                deal_cells += 1

                pass
            elif life == off_point: # 활성화 상태라면 사방을 보고 퍼질지 판단
                for k in range(4):
                    xx, yy = x+di[k], y+dj[k]
                    if dead_board.get((xx,yy)):
                        continue
                    if board.get((xx, yy)) == None: # 기존 위치에 없으면 다음단계로
                        if temp_board.get((xx, yy)) == None: # 새 판에도 없으면,
                            temp_board[(xx, yy)] = [life, 0, 0] # 추가할 판에 임시추가
                            cells+=1
                        else: # 임시판에 이미 있다면, 생명력 크기 비교로 어떤 놈을 살릴지 정하라
                            if temp_board[(xx, yy)][0] < life:
                                temp_board[(xx, yy)][0] = life
                on_point += 1
                new_board[(x, y)] = [life, off_point,on_point]

            elif life > off_point: # 비활성화 상태면, 비활성화 포인트 하나 추가하고 넘어간다.
                off_point += 1
                new_board[(x, y)] = [life, off_point,on_point]

        # step2 한 사이클 돌았으면 temp를 기존 보드와 합친다. 가능?
        board={}
        board.update(new_board)
        board.update(temp_board)
        if DEBUG:
            print('round',_)
            print('dead_cells', deal_cells, 'cells',cells)
            print(board)
            print(dead_board)

    # 마지막 시점에서 다시한번 죽은 애들을 카운트 해준다.
    for xy, lis in board.items():
        x, y = xy[0], xy[1]
        life, off_point, on_point = lis[0], lis[1], lis[2]
        if life == off_point == on_point:
            deal_cells+=1
            continue

    print('#%s %s' % (t,cells-deal_cells))




