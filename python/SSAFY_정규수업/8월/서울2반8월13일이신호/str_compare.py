T = int(input())

for tc in range(1, T+1):
    first = input()
    second = input()
    result = 0
    for i in range(len(second)-len(first)+1):
        count = 0
        for j in range(len(first)):          
            if first[j] == second[i+j]:
                count += 1
                
        
        if count == len(first):
            result = 1
            break
        

    print('#{} {}'.format(tc, result))

