arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0,5,4,1,1,2,0]

def solution(arrows):
        # 0   1   2  3  4  5  6   7

    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]
    dic = {}
    i, j = 0, 0
    count = 0
    for arrow in arrows:  # 각 방향마다 좌표값을 저장한다.
        for _ in range(2):

            ii = i + di[arrow]  # 새로운 i
            jj = j + dj[arrow]  # 새로운 j
            # if (ii, jj) in dic[(i, j)] :
            #     continue
            if (i, j) not in dic:
                dic[(i, j)] = {(ii, jj)}
                if (ii, jj) not in dic:
                    dic[(ii, jj)] = {(i, j)}
                    # print(dic)
                    # break
                else:
                    count += 1
                    dic[(ii, jj)].add((i, j))

            else:  # i, j 가 기존에 dic 안에 있다면,
                if (ii, jj) in dic[(i, j)]:
                    count -= 1
                dic[(i, j)].add((ii, jj))
                if (ii, jj) not in dic:
                    dic[(ii, jj)] = {(i, j)}

                else:
                    count += 1
                    dic[(ii, jj)].add((i, j))

            i = ii
            j = jj
    # print(dic)
    return count

print(solution(arrows))