def solution(numbers, hand):
    def dist(y, x, yy, xx):
        return abs(yy-y) + abs(xx-x)

    arr = [1,2,3,4,5,6,7,8,9,'*',0,'#']
    mat = [[0,0,0] for _ in range(4)]
    dic = {}
    print(mat)
    for i in range(4):
        for j in range(3):
            mat[i][j] = arr[3 * i+j]
            dic[arr[3*i+j]] = (i,j)
    print(dic)
    print(mat)
        # y, x
    left = (3, 0)
    right = (3, 2)

    answer = ''
    for num in numbers:
        if num in (1, 4, 7):
            answer += 'L'
            left = dic[num]
        elif num in (3, 6, 9):
            answer += 'R'
            right = dic[num]
        else:
            y, x = dic[num]
            temp1 = dist(y, x, left[0], left[1])
            temp2 = dist(y, x, right[0], right[1])
            if temp1 == temp2:
                if hand == 'right':
                    answer += 'R'
                    right = dic[num]
                else:
                    answer += 'L'
                    left = dic[num]
            elif temp1 < temp2:
                answer += 'L'
                left = dic[num]
            else:
                answer += 'R'
                right = dic[num]
    return answer


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")