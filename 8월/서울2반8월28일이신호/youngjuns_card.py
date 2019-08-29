

T = int(input())
for tc in range(1, T+1):
    try:
        cards = input()
        cards_list = []

        S = 13
        D = 13
        H = 13
        C = 13

        for i in range(0, len(cards), 3):
            s = ''
            for j in range(3):
                s += cards[i+j]
            cards_list += [s]
            if s[0] == 'S':
                S -= 1
            elif s[0] == 'D':
                D -= 1
            elif s[0] == 'H':
                H -= 1
            elif s[0] == 'C':
                C -= 1
        # print(cards_list)

        # error 찾기
        for ii in range(len(cards_list) - 1):
            for jj in range(ii, len(cards_list)):
                if ii < jj:
                    if cards_list[ii] == cards_list[jj]:
                        raise ValueError

        print('#{} {} {} {} {}'.format(tc, S, D, H, C))


    except ValueError:
        print('#{} EROOR'.format(tc))