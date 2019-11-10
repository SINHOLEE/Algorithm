
s = "{{20,111},{111},{20,33,111}}"

def solution(s):
    max_item = 0
    tuples = []
    s = s[1:-1]
    for i in range(len(s)):
        if s[i] == '{':
            is_digit = False
            digit = ''
            cnt = 0
            temp = []
        elif s[i] == '}':
            tuples.append([len(temp), temp])
        elif s[i] == ',':
            if is_digit:
                is_digit = False
                cnt += 1
                temp.append(int(digit))
                digit = ''
            continue
        else:
            is_digit = True
            if is_digit:
                digit += s[i]
                if s[i+1] == '}':
                    is_digit = False
                    cnt += 1
                    temp.append(int(digit))
                    digit = ''
    tuples.sort()
    answer = []
    for t in range(len(tuples)):
        for i in tuples[t][1]:
            if i not in answer:
                answer.append(i)
                break
    return  answer

print(solution(s))