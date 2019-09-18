def isTriple(counts):
    for i in range(8):
        cnt = 0
        for j in range(3):
            if counts[i+j] == 0:
                continue
            else:
                cnt += 1
        if cnt == 3:
            return True
    return False

def isRun(counts):
    for count in counts:
        if count == 3:
            return True
    return False
T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, input().split()))

    player1 = []
    player2 = []
    player1_count = [0] * 10
    player2_count = [0] * 10
    for card_idx in range(len(cards)):
        if card_idx % 2: # 플레이어2가 가져감
            player2.append(cards[card_idx])
            player2_count[cards[card_idx]] += 1
            if isTriple(player2_count) or isRun(player2_count):
                print('#%s 2' % tc)
                break
        else:
            player1.append(cards[card_idx])
            player1_count[cards[card_idx]] += 1
            if isTriple(player1_count) or isRun(player1_count):
                print('#%s 1' % tc)
                break
    else:
        print('#%s 0' % tc)
