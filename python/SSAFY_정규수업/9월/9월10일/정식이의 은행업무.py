def bin_check(b_n):
    possible_digit = []
    dec_digit = int('0b'+b_n, 2)
    for i in range(len(b_n)-1 ,-1 ,-1):
        # print(i, b_n[i])
        if b_n[i] == '1':
            new = dec_digit - (2**(len(b_n)-1-i))
            possible_digit.append(new)
        else:
            new = dec_digit + (2 ** (len(b_n)-1-i))
            possible_digit.append(new)
    # print(possible_digit)
    return possible_digit

def tri_check(t_n):
    possible_digit = []
    dec_digit = 0
    for i in range(len(t_n)):
        dec_digit += int(t_n[i]) * (3**(len(t_n)-1-i))
    # print(dec_digit)
    for j in range(len(t_n)-1, -1, -1):
        # print(t_n[j], j)
        if t_n[j] == '0':
            for k in range(1,3):
                new = dec_digit + (3 ** (len(t_n)-1-j)) * k
                possible_digit.append(new)
        elif t_n[j] == '1':
            for kk in range(2):
                if kk == 0: # 0으로
                    new = dec_digit - (3 ** (len(t_n) - 1 - j))
                    possible_digit.append(new)
                else:
                    new = dec_digit + (3 ** (len(t_n) - 1 - j))
                    possible_digit.append(new)
        else:
            for kkk in range(1,3):
                new = dec_digit - (3 ** (len(t_n) - 1 - j)) * kkk

                possible_digit.append(new)
    # print(possible_digit)
    return possible_digit

T = int(input())

for tc in range(1, T+1):
    bin_num = str(input())
    tri_num = str(input())

    bin_list = bin_check(bin_num)
    tri_list = tri_check(tri_num)

    # print(bin_list)
    # print(tri_list)

    for dec_num in bin_list:
        if dec_num in tri_list:
            print('#%s %s' %(tc, dec_num))
            break