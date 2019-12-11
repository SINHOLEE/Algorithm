S = 'baadasdasfadsgsaa'
def solution(S):
    string = ''
    flag = True
    a_cnt = 0
    for char in S:
        if char == 'a':
            a_cnt += 1
            if a_cnt == 3:
                flag = False
                break
            string += char
        else:
            while a_cnt < 2:
                string += 'a'
                a_cnt+=1
            string += char
            a_cnt = 0
    if flag:
        while a_cnt < 2:
            string += 'a'
            a_cnt += 1
    return len(string) - len(S) if flag else -1
print(solution(S))
