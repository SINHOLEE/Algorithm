def solution(answer_sheet, sheets):
    length = len(answer_sheet)
    dic = {}
    for i in range(length):

        visited = [1] * len(sheets)
        for j in range(len(sheets)):

            if answer_sheet[i] == sheets[j][i]:
                visited[j] = 0

        for k in range(len(visited)-1):
            for kk in range(k+1, len(visited)):
                # 둘 다 틀렸으면서 서로 같다면 == 의심문항
                if visited[k] and visited[kk]:
                    if sheets[k][i] == sheets[kk][i]:
                        if dic.get((k, kk)) is None:
                            #총개수, 최대값, 연속여부, 현재연속된 수
                            dic[(k, kk)] = [1, 1, True, 1]
                        else:
                            # 만약
                            temp = dic[(k, kk)]
                            if temp[2]:
                                dic[(k, kk)] = [temp[0]+1, max(temp[1], temp[3]+1), True, temp[3]+1]
                            else:
                                dic[(k, kk)] = [temp[0]+1, temp[1], True, 1]
                    else:
                        if dic.get((k, kk)) is not None:
                            dic[(k, kk)][2] = False
                            dic[(k, kk)][3] = 0
                else:

                    if dic.get((k, kk)) is not None:
                        dic[(k, kk)][2] = False
                        dic[(k, kk)][3] = 0



        res = 0
        for k, item in dic.items():
            temp = item[0] + item[1] ** 2
            if res < temp:
                res = temp


    return res


solution("53241", ["53241", "42133", "53241", "14354"])