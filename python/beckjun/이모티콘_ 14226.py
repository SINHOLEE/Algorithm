# n=int(input())

# visited = [[0]*1001 for _ in range(1001)]
# visited[1][0]=1

# queue = [(1,1,0)]
# while queue:
#     cnt, view, clip_board = queue.pop(0)
#     if view == n:
#         print(cnt-1)
#         break
#     #복사
#     if visited[view][view]==0 or visited[view][view] > cnt+1:
#         queue.append((cnt+1, view,view))
#         visited[view][view] = cnt+1
#     #삭제
#     if view>1 and (visited[view-1][clip_board] ==0 or visited[view-1][clip_board]>cnt+1):
#         queue.append((cnt+1,view-1,clip_board))
#         visited[view-1][clip_board] = cnt+1
#     #붙여넣기
#     if view+clip_board<=1000 and (visited[view+clip_board][clip_board]==0 or visited[view+clip_board][clip_board]>cnt+1):
#         queue.append((cnt+1,view+clip_board,clip_board))
#         visited[view+clip_board][clip_board] = cnt+1

def GCD(S):
    res = S-1
    while S % res != 0:
        res -= 1
    return res

def imoticon(S):
    if S <= 5:
        return S
    else:
        divider = GCD(S)
        if divider != 1:
            print(S//divider, S,divider)
            tmp = [imoticon(divider) + (S // divider)]
            
            for i in range(1, 3):
                nd = GCD(S+i)
                q2 = (S+i) // nd
                tmp.append(imoticon(nd) + q2 + i)

            return min(tmp)

        else:
            nd = GCD(S+1)
            q2 = (S+1) // nd
            c = imoticon(nd) + q2 + 1
            return c

S = int(input())
print(imoticon(S))
