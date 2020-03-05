import sys
input = sys.stdin.readline
DEBUG=False
n = int(input())


mat = [[*map(int, input().strip().split())] for _ in range(n)]
        #-1 0 1
bucket = [0,0,0]

def divided(board, length):
    if length == 1:
        if board[0][0] == -1:
            bucket[0] += 1
        elif board[0][0] == 0:
            bucket[1] += 1
        else:
            bucket[2] += 1
        return
    flag = False
    first = board[0][0]
    for i in range(length):
        for j in range(length):
            if board[i][j] == first:
                continue
            else:
                flag = True
                break
        if flag:
            break
    if flag:
        # q분할:
        tri = length // 3
        for i in range(1, 4):
            for j in range(1, 4):
                temp = []

                for x in range((i - 1) * tri, (i) * tri):
                    new = []
                    for y in range((j - 1) * tri, (j) * tri):
                        new.append(board[x][y])
                    temp.append(new)
                if DEBUG:
                    print()
                    for arr in temp:
                        print(arr)
                    print('bucket',bucket)
                divided(temp, tri)
    else:
        if first == -1:
            bucket[0] += 1
        elif first == 0:
            bucket[1] += 1
        else:
            bucket[2] += 1
        return
divided(mat,n)
print(bucket[0])
print(bucket[1])
print(bucket[2])