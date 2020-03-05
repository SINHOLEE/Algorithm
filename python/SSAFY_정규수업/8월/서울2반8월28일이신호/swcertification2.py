

T = int(input())
def shuffle(li, i):
    new = []
    mid = len(li) // 2
    L_cards = li[0: mid]
    R_cards = li[mid:]

    if i >= mid:
        while True:
            if len(new) == len(li):
                break
            for y in range(i - mid + 1):
                a = R_cards.pop(0)
                new.append(a)
            for x in range(1):
                a = L_cards.pop(0)
                new.append(a)

            while True:
                if len(L_cards) == 0 and len(R_cards) == 0:
                    break
                if len(R_cards) == 0:
                    pass
                else:
                    a = R_cards.pop(0)
                    new.append(a)
                if len(L_cards) == 0:
                    pass
                else:
                    a = L_cards.pop(0)
                    new.append(a)


    else:
        while True:
            if len(new) == len(li):
                break
            for x in range(mid - i):
                a = L_cards.pop(0)
                new.append(a)
            for y in range(1):
                a = R_cards.pop(0)
                new.append(a)
            while True:
                if len(L_cards) == 0 and len(R_cards) == 0:
                    break
                if len(L_cards) == 0:
                    pass
                else:
                    a = L_cards.pop(0)
                    new.append(a)
                if len(R_cards) == 0:
                    pass
                else:
                    a = R_cards.pop(0)
                    new.append(a)
    return new


def shuffle_card(card_list, start_idx, end_idx, mid, ):
    global count, min_cnt
    if card_list == result_b or card_list == result_a:
        if count < min_cnt:
            min_cnt = count
        return
    if count > 5:
        return
    # shuffle
    if min_cnt < count:
        pass
    else:

        for i in range(1, len(card_list)):
            new_cards = shuffle(card_list, i)

            # 섞고 나서 새로운 카드로 생성하고 카운트를 하나 추가.

            count += 1
            # 새롭게 만든 카드를 다시한번 섞는다.
            shuffle_card(new_cards, 0, len(card_list) - 1, mid)
            # 섞인게 retrun으로 돌아왔으면 전역변수인 count를 하나 줄여 depth를 맞춘다.
            count -= 1


for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    count = 0
    result_a = sorted(cards)
    result_b = sorted(cards)[::-1]
    p = N // 2
    min_cnt = 6
    shuffle_card(cards, 0, len(cards)-1, p)

    if min_cnt > 5:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc, min_cnt))

