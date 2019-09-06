from pprint import pprint

def merge(left, right):
    temp = []

    while True:
        if len(left) == 0 or len(right) == 0:
            break
        if left[0][0] < right[0][0]:
            temp.append(left.pop(0))
        elif left[0][0] > right[0][0]:
            temp.append(right.pop(0))
        else:
            if left[0][1] <= right[0][1]:
                temp.append(left.pop(0))
            else:
                temp.append(right.pop(0))
    if len(left) == 0:
        while True:
            if len(right) == 0:
                break
            temp.append(right.pop(0))
    if len(right) == 0:
        while True:
            if len(left) == 0:
                break
            temp.append(left.pop(0))


    return temp




def divided_sort(li):
    if len(li) <= 1:
        return li

    mid = len(li) // 2

    left = divided_sort(li[:mid])
    right = divided_sort(li[mid:])


    return merge(left, right)


#
#

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    mat = []
    visited = []
    for n in range(N):
        temp = list(map(int, input().split()))
        temp1 = [False] * N
        mat.append(temp)
        visited.append(temp1)
    #
    # pprint(mat)
    # pprint(visited)
    bucket = []
    for i in range(N):
        for j in range(N):
            if mat[i][j] != 0 and visited[i][j] == False:
                row_count = 0
                total_count = 0
                for ii in range(i, N):
                    if mat[ii][j] != 0 and visited[ii][j] == False:
                        row_count += 1
                        for jj in range(j, N):
                            if mat[ii][jj] != 0 and visited[ii][jj] == False:
                                visited[ii][jj] = True
                                total_count += 1
                            else:
                                break
                    else:
                        break
                bucket.append([total_count, row_count, total_count // row_count])


    # bucket = divided_sort(bucket)

    # bucket = sorted(bucket)


    print('#{} {}'.format(tc, len(bucket)), end = ' ')
    for element in bucket:
        for i in range(1, len(element)):
            print('{}'.format(element[i]), end = ' ')
    print()

