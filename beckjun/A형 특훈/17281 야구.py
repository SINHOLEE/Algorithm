from pprint import pprint
#
def perm(depth, ordered_player):
    global max_score
    if depth == 9:
        score = 0
        current_player_index = 0
        for i in range(n):
            # 매 이닝 마다 관리한다.
            outScore = 0
            locations = [0] * 9  # 각
            roo = set()
            while True:
                if outScore == 3:
                    break
                player = ordered_player[current_player_index]  #
                batTogo = play_data[i][player]  # 이만 큼 갈 수 있다는 뜻

                if batTogo:
                    del_list = set()
                    roo.add(player)
                    for p in roo:
                        locations[p] += batTogo
                        if locations[p] >= 4:
                            score += 1
                            locations[p] = 0
                            del_list.add(p)
                    roo = roo - del_list

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
        return
    for i in range(1, 10):
        if i == 1:
            continue
        if visited[i-1] == False and depth == 3:
            perm(depth + 1, ordered_player + [0])
        elif visited[i-1] == False and depth != 3:
            visited[i-1] = True
            perm(depth + 1, ordered_player + [i-1])
            visited[i-1] = False


max_score = 0
n = int(input())
play_data = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * 9
perm(0, [])

print(max_score)

# 처음엔 밖에서 관리되고 그 다음부터는 안에서 관리된다.

