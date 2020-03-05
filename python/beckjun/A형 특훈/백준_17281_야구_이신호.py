#
max_score = 0
n = int(input())
play_data = [list(map(int, input().split())) for _ in range(n)]
#

# 처음엔 밖에서 관리되고 그 다음부터는 안에서 관리된다.

ordered_player = [1, 2, 3, 4, 5, 6, 7, 8]
stop = False
while True:
    new_list = ordered_player[:3] + [0] + ordered_player[3:]
    score = 0
    current_player_index = 0
    for k in range(n):
        # 매 이닝 마다 관리한다.
        outScore = 0
        roo_a, roo_b, roo_c = 0,0,0
        while True:
            if outScore == 3:
                break
            player = new_list[current_player_index]  #
            batTogo = play_data[k][player]  # 이만 큼 갈 수 있다는 뜻

            if batTogo:
                if batTogo == 4:
                    score += 1+roo_a+roo_b+roo_c
                    roo_a,roo_b,roo_c = 0,0,0
                elif batTogo == 3:
                    score += roo_a+roo_b+roo_c
                    roo_a,roo_b,roo_c = 0,0, 1
                elif batTogo == 2:
                    score += roo_b+roo_c
                    roo_a,roo_b,roo_c = 0,1,roo_a
                elif batTogo == 1:
                    score += roo_c
                    roo_a,roo_b,roo_c = 1,roo_a, roo_b
            else:
                outScore += 1

            current_player_index = (current_player_index + 1) % 9
            # print(roo)
            # print(locations)
            # print(current_player_index)
            # print(i, outScore, score)
            # print()
    if max_score < score:
        max_score = score

    for i in range(7,-1,-1):
        if i == 0:
            stop = True
            break
        if ordered_player[i-1] < ordered_player[i]:
            idx = i-1
            break
    if stop:
        break
    for i in range(7, -1, -1):
        if ordered_player[idx] < ordered_player[i]:
            target = i
            ordered_player[idx], ordered_player[target] = ordered_player[target],ordered_player[idx]
            break
    idx += 1
    end = 7
    while True:
        if idx >= end:
            break
        ordered_player[idx], ordered_player[end] = ordered_player[end], ordered_player[idx]
        idx += 1
        end -= 1

print(max_score)
