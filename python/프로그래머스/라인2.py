def solution(answer_sheet, sheets):
    length = len(answer_sheet)
    dic = {}
    for i in range(length):
        print(answer_sheet[i])
        bucket = []
        for j in range(len(sheets)):
            print(sheets[j][i])
            if answer_sheet[i] != sheets[j][i]:
                bucket.append((j, i))

        print(bucket)
        for k in range(len(bucket) - 1):
            for kk in range(k + 1, len(bucket)):

                if sheets[bucket[k][0]][bucket[k][1]] == sheets[bucket[kk][0]][bucket[kk][1]]:
                    if dic.get((bucket[k][0], bucket[kk][0])) is None:
                        dic[(bucket[k][0], bucket[kk][0])] = 1
                    else:
                        dic[(bucket[k][0], bucket[kk][0])] += 1
        print()
        print(dic)
    answer = -1
    return answer


solution("4132315142", ["3241523133", "4121314445", "3243523133", "4433325251", "2412313253"])