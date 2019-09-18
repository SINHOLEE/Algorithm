participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for i in participant:
       dic[id(i)] = i
       temp += id(i)
    for c in completion:
        temp -= id(c)
    answer = dic[temp]

    return answer
print(solution(participant, completion))

