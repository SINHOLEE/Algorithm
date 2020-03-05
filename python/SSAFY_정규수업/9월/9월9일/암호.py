from pprint import pprint

def change(string):
    if string == '0001101':
       return 0
    elif string == '0011001':
        return 1
    elif string == '0010011':
        return 2
    elif string == '0111101':
        return 3
    elif string == '0100011':
        return 4
    elif string == '0110001':
        return 5
    elif string == '0101111':
        return 6
    elif string == '0111011':
        return 7
    elif string == '0110111':
        return 8
    elif string == '0001011':
        return 9
    else:
        return 'a'

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # n 은 row, m 은col
    mat= []
    for n in range(N):
        temp = input()
        if '1' not in temp:
            continue
        mat.append(temp)
        break
    # pprint(mat)

    check = False
    for search in range(len(mat)-1):
        if mat[search] != mat[search+1]:
            result = 0
            check = True
            break
    if not check:
        for i in range(len(mat[0])-1, -1, -1):
            if mat[0][i] == '1':
                last_index = i + 1
                start_index = i - 56 + 1
                # print(start_index)
                # print(last_index)
                break
        # print(len(mat[0][start_index:last_index]))
        # print(mat[0][start_index:last_index])
        password = mat[0][start_index:last_index]

        disit_list = []
        for pas in range(0, len(password), 7):
            str_digit = password[pas:pas +  7]
            int_digit = change(str_digit)
            disit_list.append(int_digit)
        # print(disit_list)
        check_decade = 3 * (disit_list[0] + disit_list[2] + disit_list[4] + disit_list[6]) + disit_list[1] + disit_list[3] + disit_list[5] + disit_list[7]
        # print(check_decade)


        try:
            if check_decade % 10 == 0:
                result = sum(disit_list)
                print('#%s %s' % (tc, result))
            else:
                result = 0
                print('#%s %s' % (tc, result))

        except:
            result = 0
            print('#%s %s' % (tc, result))
