from pprint import pprint

mat = [[1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
      [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
      [1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
      [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
      [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
      [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
      [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
      [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
      [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
      [1, 0, 2, 0, 1, 0, 0, 0, 0, 1]]
    # 좌 우 하
id = [0, 0, 1]
jd = [-1, 1, 0]
# j = 우리가 원하는 인덱스
def iswall(i, j):
    if i < 0 or i > 9 or j < 0 or j > 9:
        return True
    else:
        return False
stop = 1
while stop:

    for j in range(len(mat[0])):
        if mat[0][j]:
            start = j
            i = 0

            direction_i = []
            direction_j = []
            done = 1
            while done:
                x = 0
                y = 0
                for k in range(3):
                    i += id[k]
                    j += jd[k]
                    if k < 2:
                        if iswall(i, j):
                            i -= id[k]
                            j -= jd[k]
                        else:
                            if x == 0:
                                direction_i += [id[k]]
                                direction_j += [jd[k]]
                                x += 1
                            else:

                                mat[i][j] == 1:
                                x += 1
                                direction_i += [id[k]]
                                direction_j += [jd[k]]
                            else:
                                i -= id[k]
                                j -= jd[k]

                    else:


                    # if k < 2:
                    #     i += id[k]
                    #     j += jd[k]
                    #
                    #     if iswall(i, j):
                    #
                    #         i -= id[k]
                    #         j -= jd[k]
                    #
                    #     elif mat[i][j] == 0:
                    #
                    #         i -= id[k]
                    #         j -= jd[k]
                    #         y += 1
                    #     elif y == 2:
                    #         i += direction_i
                    #         j += direction_j
                    #     else:
                    #         x = 1
                    #
                    #
                    # else:
                    #     if x == 1:
                    #         pass
                    #     else:
                    #         i += id[2]
                    #         j += jd[2]
                    #         if iswall(i, j):
                    #             done = 0
                    #         else:
                    #             i -= id[2]
                    #             j -= jd[2]
                    #             if mat[i][j] == 2:
                    #                 stop = 0
                    #                 done = 0
                    #             else:
                    #                 i += id[2]
                    #                 j += jd[2]
                print(i, j, mat[i][j], '현재위치')

                        # if (not iswall(i, j))and mat[i][j] == 2:
                        #     stop = 0
                        # if iswall(i, j):
                        #     stop = 0
                        #     done = 0
                        # else:
                        #     if mat[i][j] == 2:
                        #         stop = 0
                        #     else:
                        #         pass

print(start)



#
