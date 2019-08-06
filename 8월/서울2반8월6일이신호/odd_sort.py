T = int(input())

for tc in range(1, T+1):
    N = int(input())
    temp = list(map(int, input().split()))

    
    for k in range(len(temp)-1):
        my_min = 100
        my_max = 0
        min_index = 0
        max_index = 0
        for i in range(k,len(temp)):
            if k % 2 == 0:
                if my_max < temp[i]:
                    my_max = temp[i]
                    max_index = i
                else:
                    pass
            
            else:
                if my_min > temp[i]:
                    my_min = temp[i]
                    min_index = i
        if k % 2 == 0:
            temp[k], temp[max_index] = temp[max_index], temp[k]
        else:
            temp[k], temp[min_index] = temp[min_index], temp[k]
    
    temp = temp[:10]
    result = ' '.join(map(str, temp))
    print('#{} {}'.format(tc, result))