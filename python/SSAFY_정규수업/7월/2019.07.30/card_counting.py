T = int(input())

for t in range(1, T + 1):
    N = int(input())
    cards = input()
    index = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(cards)):
    #     # num = int(cards[i])
        num = int(cards[i])
    #
        index[num] += 1
    #
        # print(index[num], type(index[num]))
    #

    # index[1] += 1

    max_count = 0
    max_index = 0
    for a in range(len(index)):
        if max_count <= index[a]:
            max_index = a
            max_count = index[a]

        else:
            pass


    print('#{} {} {}'.format(t, max_index, max_count))