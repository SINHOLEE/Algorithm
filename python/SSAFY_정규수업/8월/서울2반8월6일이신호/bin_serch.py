def c(l,r):
    return int((l + r)/2)

T = int(input())

for tc in range(1, T+1):
    r ,pa, pb = input().split()
    r, pa, pb = int(r), int(pa), int(pb)

    count_a, count_b = 0, 0
    result = 0
    l_a = 1
    l_b = 1
    r_a = r
    r_b = r
    c_a = c(l_a, r)
    c_b = c(l_b, r)
    stop_a = 0
    stop_b = 0
    while (True) :
        
        if stop_a == 1 and stop_b == 1:
            break

        else:              
            if c_a < pa:
                l_a = c_a
                count_a += 1
                c_a = c(l_a,r_a)
            elif c_a > pa:
                r_a = c_a
                count_a += 1
                c_a = c(l_a, r_a)
            elif c_a == pa:
                stop_a = 1
            
            if c_b < pb:
                l_b = c_b
                count_b += 1
                c_b = c(l_b, r_b)
            elif c_b > pb:
                r_b = c_b
                count_b += 1
                c_b = c(l_b, r_b)
            elif c_b == pb:
                stop_b = 1
            
    if count_a < count_b:
        result = 'A'
    elif count_a > count_b:
        result = 'B'
    else:
        result = 0      
    print('#{} {}'.format(tc, result))
