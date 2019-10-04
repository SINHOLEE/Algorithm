n = 7
results = [[1, 2], [4, 2], [1, 5], [2, 3],[5,3],[5,6],[3,6],[3,7],[6,7]]

def solution(n, results):
    fight = [[set(),_ ,set(), 0] for _ in range(n)]
    for win, lose in results:
        fight[win - 1][2].add(lose - 1)
        fight[win - 1][3] += 1
        fight[lose - 1][0].add(win - 1)
        fight[lose - 1][3] += 1
    print(fight)
    for front, i ,back, cnt in fight:
        for w in front:
            fight[w][2].add(i)
            fight[w][2].update(back)

            fight[w][3] = len(fight[w][2]) + len(fight[w][0])
        for l in back:
            fight[l][0].add(i)
            fight[l][0].update(front)
            fight[l][3] = len(fight[l][2]) + len(fight[l][0])
        print(fight)
    # print(fight)
    return len(list(filter(lambda x: x[3] == n-1, fight)))

print(solution(n, results))